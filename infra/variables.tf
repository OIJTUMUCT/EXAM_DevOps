variable "folder_id" {
  description = "ID папки Yandex Cloud"
  type        = string
}

variable "registry_id" {
  description = "ID Container Registry (используется для документации/локального запуска)"
  type        = string
}

variable "service_account_id" {
  description = "ID сервисного аккаунта, от имени которого работает serverless container"
  type        = string
}

variable "image_tag" {
  description = "Полный URL Docker-образа для serverless-контейнера"
  type        = string
}