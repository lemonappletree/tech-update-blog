# 🛠️ 2025-08-05 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.34 Sneak Peek
The blog post previews Kubernetes v1.34, set for release at the end of August 2025, and highlights several exciting enhancements without any deprecations. Key features include:

1. **Dynamic Resource Allocation (DRA)**: Targeting stable status, DRA allows flexible device management with structured parameters for GPUs and custom hardware.
   
2. **ServiceAccount Tokens for Image Pull Authentication**: Likely reaching beta, this feature helps kubelet use ServiceAccount tokens for registry authentication, enhancing security and reducing operational overhead.

3. **Pod Replacement Policy for Deployments**: Introduced as alpha, this feature allows control over pod replacement timing during updates, providing options for faster rollouts or controlled resource usage.

4. **Production-ready Tracing**: Enhancements for kubelet and API Server tracing aim for stable release, offering improved debugging capabilities and end-to-end event visibility.

5. **Traffic Distribution Preferences**: New `PreferSameZone` and `PreferSameNode` options for service traffic routing are moving to beta, allowing more granular control over traffic distribution.

6. **Support for KYAML**: A Kubernetes-specific YAML subset, KYAML, enhances safety and clarity, expected as a new output format in kubectl v1.34.

7. **HPA Configurable Tolerance**: This feature allows per-HPA tolerance settings for autoscaling, moving to beta for more responsive and efficient scaling.

The post encourages community involvement through Special Interest Groups (SIGs), discussions, and contributing to the Kubernetes community. The official release notes will announce further details, and the release is scheduled for August 27, 2025.
👉 [Read more](https://kubernetes.io/blog/2025/07/28/kubernetes-v1-34-sneak-peek/)

## 🔹 Spring Boot - Spring Shell 3.4.1 is now available
The blog post announces the release of Spring Shell version 3.4.1, which is now available on Maven Central. This update includes several bug fixes, dependency updates, and improvements to the documentation. The release notes provide detailed information about the changes. The post also expresses gratitude to contributors who reported issues and submitted pull requests. It includes links to the project page, GitHub repository, issue tracker, and documentation for those interested in contributing or learning more.
👉 [Read more](https://spring.io/blog/2025/08/04/spring-shell-3-4-1-available)

## 🔹 Docker - How Docker MCP Toolkit Works with VS Code Copilot Agent Mode
The blog post discusses the integration of Docker's Model Context Protocol (MCP) Toolkit with Visual Studio Code’s GitHub Copilot Agent Mode, highlighting its impact on software development. This integration represents a significant advancement in improving productivity and the developer experience by leveraging modern AI tools. By combining these technologies, developers can interact more effectively with containerized applications, facilitating a more autonomous development process. The post explores how this powerful combination transforms workflows, making it an essential tool in the evolving landscape of software development.
👉 [Read more](https://www.docker.com/blog/mcp-toolkit-and-vs-code-copilot-agent/)

## 🔹 Java - JavaOne: Returning to the Bay Area March 17-19, 2026
The blog post announces the return of the JavaOne conference, which will be held in the Bay Area from March 17-19, 2026. It highlights that the previous year's event was successful and anticipates another outstanding experience for attendees this year.
👉 [Read more](https://inside.java/2025/08/04/javaone-returns-2026/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
The blog post discusses a new feature in the Go programming language: a built-in, native mode that complies with the FIPS 140-3 standard, which is a U.S. government standard for cryptographic modules. This addition is significant for developers who require FIPS compliance for security-sensitive applications, as it ensures that cryptographic operations in Go meet stringent federal standards. The post likely elaborates on the implementation details, benefits, and how developers can utilize this new mode in their Go applications.
👉 [Read more](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London, UK, from April 1 to 4. Attendees can engage with Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion. The post highlights that Helm 4 is currently in development, and attendees are encouraged to participate in discussions about it. More details about Helm-related activities during the event can be found in the post.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

