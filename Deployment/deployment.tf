provider "kubernetes" {
  config_path = "~/.kube/config"  # Path to your kubeconfig
}

# Deploy Backend Deployment from YAML
resource "kubernetes_manifest" "backend_deployment" {
  manifest = yamldecode(file("backend.yaml"))
}


# Deploy Frontend Deployment from YAML
resource "kubernetes_manifest" "frontend_deployment" {
  manifest = yamldecode(file("frontend.yaml"))
}

# Deploy Frontend Service from YAML
resource "kubernetes_manifest" "database_deployment" {
  manifest = yamldecode(file("database.yaml"))
}
