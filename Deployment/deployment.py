from kubernetes import client, config
import subprocess
import time

def check_deployment_running(deployment_name, namespace):
    """Check if the specified deployment is available and running."""
    apps_v1 = client.AppsV1Api()
    try:
        deployment = apps_v1.read_namespaced_deployment(deployment_name, namespace)
        # Check if the available replicas match the desired replicas
        return (deployment.status.available_replicas == deployment.status.replicas and 
                deployment.status.replicas is not None)
    except client.exceptions.ApiException as e:
        print(f"Exception when checking deployment: {e}")
        return False

def apply_deployment(yaml_file):
    """Apply a deployment YAML file using kubectl."""
    try:
        subprocess.run(["kubectl", "apply", "-f", yaml_file], check=True)
        print(f"Successfully applied {yaml_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error applying {yaml_file}: {e}")

def wait_for_deployment_to_run(deployment_name, namespace, check_interval=5):
    """Wait until the specified deployment is available and running."""
    print(f"Waiting for {deployment_name} to be running...")
    while not check_deployment_running(deployment_name, namespace):
        time.sleep(check_interval)
    print(f"{deployment_name} is now running.")
def main():
    # Configuration
    target_deployment_name = "my-release-milvus-standalone"
    namespace = "default"  
    deployment_yamls = [
        ["backend-deployment","backend.yaml"],
        ["react-app-deployment","frontend.yaml"]
    ]

    wait_for_deployment_to_run(target_deployment_name, namespace)

    for yaml_file in deployment_yamls:
        apply_deployment(yaml_file)

if __name__ == "__main__":
    config.load_kube_config()  # Load kubeconfig
    main()
