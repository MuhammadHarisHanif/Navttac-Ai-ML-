# Azure AI Services Deployment

## 1. Objective

Understand how to deploy Microsoft Azure AI Services and integrate them into applications.

## 2. Azure Service Endpoints

An endpoint is a URL used by an application to communicate with an Azure AI resource.

Important information:

- Resource endpoint
- Authentication credentials
- API access
- Supported service operations

## 3. Create Resources Using Azure Portal

General steps:

1. Sign in to Azure Portal.
2. Select the required Azure AI service.
3. Create a new resource.
4. Configure subscription and resource group.
5. Select the appropriate region and pricing tier.
6. Review the configuration.
7. Deploy the resource.
8. Locate its endpoint and authentication settings.

## 4. CI/CD Integration

Continuous Integration and Continuous Deployment (CI/CD) automate application development and deployment.

Typical workflow:

1. Developer updates application code.
2. Code is pushed to a Git repository.
3. Automated build process starts.
4. Application tests are executed.
5. Deployment pipeline publishes the application.

Common tools include GitHub Actions and Azure DevOps.

## 5. Container Deployment

Containers package an application and its dependencies together.

Important concepts:

- Container images
- Docker containers
- Container configuration
- Environment variables
- Network connectivity
- Resource requirements

Azure AI prebuilt containers can be used for supported services when the appropriate licensing, image access and infrastructure requirements are met.

## 6. Practical Exercise

**Task:** Understand Azure AI deployment.

Steps:

1. Identify an Azure AI service.
2. Explore its resource endpoint.
3. Understand its authentication requirements.
4. Review application integration.
5. Explore CI/CD deployment concepts.
6. Understand container deployment.
7. Document the deployment workflow.

## 7. Security Considerations

- Never expose API keys.
- Store credentials securely.
- Use environment variables or managed identities where supported.
- Restrict resource access.
- Monitor deployed resources.

## 8. Conclusion

Azure AI deployment involves resource creation, endpoint configuration, application integration, CI/CD automation and container deployment.

## 9. Learning Outcome

Understand the basic process of deploying Azure AI Services and integrating them into software applications.
