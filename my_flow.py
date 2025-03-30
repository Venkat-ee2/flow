from prefect import Flow, task
from prefect.deployments import Deployment
from prefect.infrastructure.docker import DockerContainer

# Create a simple task
@task
def hello_world():
    print("Hello, world!")

# Create a flow
with Flow("hello-flow") as flow:
    hello_world()

# Register flow with Prefect Cloud (or Prefect Server)
flow.register(project_name="my_project")

# Optionally, create a deployment with Docker infrastructure
deployment = Deployment.build_from_flow(
    flow,
    name="hello-flow-deployment",
    infrastructure=DockerContainer(),  # Optional: Use Docker as infrastructure
)

# Register the deployment
deployment.apply()
