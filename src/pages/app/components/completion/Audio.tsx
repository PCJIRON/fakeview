import { InfoIcon, MicIcon, MicOffIcon } from "lucide-react";
import { Popover, PopoverContent, PopoverTrigger, Button } from "@/components";
import { AutoSpeechVAD } from "./AutoSpeechVad";
import { UseCompletionReturn } from "@/types";
import { useApp } from "@/contexts";
import { useRef, useCallback, useEffect } from "react";

export const Audio = ({
  micOpen,
  setMicOpen,
  enableVAD,
  setEnableVAD,
  submit,
  setInput,
  setState,
}: UseCompletionReturn) => {
  const { selectedSttProvider, pluelyApiEnabled, selectedAudioDevices } =
    useApp();

  const speechProviderStatus = selectedSttProvider.provider;
  const isBrowserSpeech = selectedSttProvider.provider === "browser-speech";
  const recognitionRef = useRef<any>(null);
  const silenceTimerRef = useRef<NodeJS.Timeout | null>(null);
  const userStoppedRef = useRef(false);
  const submitRef = useRef(submit);
  submitRef.current = submit;

  useEffect(() => {
    return () => {
      userStoppedRef.current = true;
      if (silenceTimerRef.current) {
        clearTimeout(silenceTimerRef.current);
      }
      if (recognitionRef.current) {
        try { recognitionRef.current.abort(); } catch {}
      }
    };
  }, []);

  const startBrowserSpeech = useCallback(() => {
    const SpeechRecognition =
      (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
    if (!SpeechRecognition) {
      setState((prev: any) => ({
        ...prev,
        error: "Browser speech not supported. Use Chrome/Edge.",
      }));
      setEnableVAD(false);
      return;
    }

    const recognition = new SpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.lang = "en-US";

    let finalText = "";

    recognition.onresult = (event: any) => {
      let interimText = "";
      for (let i = event.resultIndex; i < event.results.length; i++) {
        if (event.results[i].isFinal) {
          finalText += event.results[i][0].transcript + " ";
        } else {
          interimText += event.results[i][0].transcript;
        }
      }

      setInput((finalText + interimText).trim());

      if (silenceTimerRef.current) {
        clearTimeout(silenceTimerRef.current);
      }

      if (finalText.trim()) {
        silenceTimerRef.current = setTimeout(() => {
          const text = finalText.trim();
          finalText = "";
          if (text) {
            submitRef.current(text);
          }
        }, 1200);
      }
    };

    recognition.onerror = (event: any) => {
      if (event.error !== "aborted" && event.error !== "no-speech") {
        setState((prev: any) => ({
          ...prev,
          error: `Speech error: ${event.error}`,
        }));
      }
    };

    recognition.onend = () => {
      if (!userStoppedRef.current && finalText.trim()) {
        submitRef.current(finalText.trim());
      }
      // Auto-restart recognition if user didn't stop it
      if (!userStoppedRef.current) {
        try {
          recognition.start();
        } catch {}
        return;
      }
      userStoppedRef.current = false;
    };

    userStoppedRef.current = false;
    recognitionRef.current = recognition;
    recognition.start();
  }, [setInput, setState, setEnableVAD]);

  const stopBrowserSpeech = useCallback(() => {
    userStoppedRef.current = true;
    if (silenceTimerRef.current) {
      clearTimeout(silenceTimerRef.current);
      silenceTimerRef.current = null;
    }
    if (recognitionRef.current) {
      try { recognitionRef.current.abort(); } catch {}
      recognitionRef.current = null;
    }
  }, []);

  const handleMicClick = () => {
    if (isBrowserSpeech) {
      if (enableVAD) {
        stopBrowserSpeech();
        setEnableVAD(false);
      } else {
        setEnableVAD(true);
        startBrowserSpeech();
      }
    } else {
      setEnableVAD(!enableVAD);
    }
  };

  // Start browser speech when enableVAD becomes true (e.g. via keyboard shortcut)
  useEffect(() => {
    if (isBrowserSpeech && enableVAD && !recognitionRef.current) {
      startBrowserSpeech();
    }
    if (isBrowserSpeech && !enableVAD && recognitionRef.current) {
      stopBrowserSpeech();
    }
  }, [isBrowserSpeech, enableVAD, startBrowserSpeech, stopBrowserSpeech]);

  return (
    <Popover open={micOpen} onOpenChange={setMicOpen}>
      <PopoverTrigger asChild>
        {(pluelyApiEnabled || speechProviderStatus) && !isBrowserSpeech && enableVAD ? (
          <AutoSpeechVAD
            key={selectedAudioDevices.input.id}
            submit={submit}
            setState={setState}
            setEnableVAD={setEnableVAD}
            microphoneDeviceId={selectedAudioDevices.input.id}
          />
        ) : (
          <Button
            size="icon"
            onClick={handleMicClick}
            className="cursor-pointer"
            title={
              isBrowserSpeech && enableVAD
                ? "Listening (autodetect)... click to stop"
                : isBrowserSpeech
                  ? "Free voice input (browser speech, no API key)"
                  : "Toggle voice input"
            }
          >
            {isBrowserSpeech && enableVAD ? (
              <MicOffIcon className="h-4 w-4 animate-pulse text-green-500" />
            ) : (
              <MicIcon className="h-4 w-4" />
            )}
          </Button>
        )}
      </PopoverTrigger>

      <PopoverContent
        align="end"
        side="bottom"
        className={`w-80 p-3 ${
          pluelyApiEnabled || speechProviderStatus ? "hidden" : ""
        }`}
        sideOffset={8}
      >
        <div className="text-sm select-none">
          <div className="font-semibold text-orange-600 mb-1">
            Speech Provider Configuration Required
          </div>
          <p className="text-muted-foreground">
            {!speechProviderStatus ? (
              <>
                <div className="mt-2 flex flex-row gap-1 items-center text-orange-600">
                  <InfoIcon size={16} />
                  {selectedSttProvider.provider ? null : (
                    <p>PROVIDER IS MISSING</p>
                  )}
                </div>

                <span className="block mt-2">
                  Please go to settings and configure your speech provider to
                  enable voice input.
                </span>
              </>
            ) : null}
          </p>
        </div>
      </PopoverContent>
    </Popover>
  );
};
