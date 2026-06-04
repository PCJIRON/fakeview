export interface TYPE_PROVIDER {
  id?: string;
  name?: string;
  streaming?: boolean;
  responseContentPath?: string;
  isCustom?: boolean;
  isBuiltIn?: boolean;
  curl: string;
}
