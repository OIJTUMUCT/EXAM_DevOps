terraform {
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = ">= 0.110.0"
    }
  }
}

provider "yandex" {
  zone                     = "ru-central1-a"
  folder_id                = var.folder_id
  # этот файл создаст GitHub Actions из секрета YC_SA_JSON_KEY
  service_account_key_file = "${path.module}/sa-key.json"
}

# serverless container для FastAPI-iris API
resource "yandex_serverless_container" "iris_api" {
  name               = "iris-api-container"
  memory             = 512
  cores              = 1
  execution_timeout  = "30s"
  service_account_id = var.service_account_id

  image {
    # полный URL образа приходит из GitHub Actions
    # пример: cr.yandex/<registry_id>/iris-api:<sha>
    url = var.image_tag
  }
}

# публичный доступ (анонимный invoke)
resource "yandex_serverless_container_iam_binding" "invoker" {
  container_id = yandex_serverless_container.iris_api.id
  role         = "serverless.containers.invoker"
  members      = ["system:allUsers"]
}

# output — публичный URL
output "iris_api_url" {
  value = "https://${yandex_serverless_container.iris_api.id}.containers.yandexcloud.net"
}