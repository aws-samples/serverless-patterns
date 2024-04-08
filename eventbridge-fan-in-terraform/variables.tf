variable "buses" {
  type        = list(string)
  description = "Name of the first EventBus"
  sensitive = true
}

variable "centralEB" {
  type        = string
  default     = "centralEB"
  description = "Name of central EventBus"
}
