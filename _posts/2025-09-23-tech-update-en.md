# 🛠️ 2025-09-23 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.34: Pod Level Resources Graduated to Beta
The blog post announces that the Pod Level Resources feature in Kubernetes has reached Beta in the v1.34 release and is now enabled by default. This feature allows users to define CPU and memory resources for an entire Pod, rather than just at the container level, offering enhanced flexibility and efficiency in resource management. Pod-level specifications reduce the need for detailed per-container management and enable better resource sharing among containers within a Pod, preventing bottlenecks and ensuring efficient operation during demand spikes. This feature also impacts scheduling, prioritizes Pod-level resources for Quality of Service classification, and ensures compatibility with existing Kubernetes functionalities. However, it does not support in-place resizing, applies only to CPU, memory, and hugepages, does not support Windows Pods, and is not managed by certain Kubernetes resource managers. Users are encouraged to provide feedback as the feature progresses through its Beta phase.
👉 [Read more](https://kubernetes.io/blog/2025/09/22/kubernetes-v1-34-pod-level-resources/)

## 🔹 Spring Boot - Spring AI 1.1.0-M2 Available Now: Enhanced Model Context Protocol Support
The blog post announces the release of Spring AI 1.1.0-M2, which is now available on Maven Central. This milestone release primarily enhances the Model Context Protocol (MCP) support by integrating updates from MCP Java SDK v0.13.0. The release includes 56 improvements covering MCP enhancements, integration fixes, new features, stability improvements, and documentation updates. Key updates include upgrading to MCP Java SDK v0.13.1, improved MCP annotations, fixes for stateless server registration, enhanced tool management, and streamlined configuration. Additional enhancements include Docker Compose support, Testcontainers integration, and several new features across various functional areas. The release also acknowledges the contributions of community members and developers from organizations like Broadcom, Oracle, and Google.
👉 [Read more](https://spring.io/blog/2025/09/19/spring-ai-1-1-0-M2-mcp-focused)

## 🔹 Docker - Silent Component Updates & Redesigned Update Experience
The blog post discusses a new feature in Docker Desktop 4.46 that introduces automatic component updates and a redesigned update experience. This enhancement aims to improve the way Docker Desktop delivers updates, ensuring that development tools are kept up to date seamlessly. The update prioritizes user productivity by implementing silent updates that occur in the background, minimizing disruption to the user's workflow. This change is part of Docker's ongoing efforts to enhance the update process for its users.
👉 [Read more](https://www.docker.com/blog/docker-desktop-silent-component-updates/)

## 🔹 Java - Paths to Support Additional Numeric Types on the Java Platform #JVMLS
The blog post discusses the need for additional numeric types in the Java platform to support scientific, engineering, and machine learning computations, which often require complex numbers and smaller numeric types like 16-bit and potentially 8-bit floating-point numbers. The talk explores the requirements and considerations for integrating these new numeric types into Java, highlighting the benefits and trade-offs of different approaches to achieve this support.
👉 [Read more](https://inside.java/2025/09/21/jvmls-java-additional-numeric-types/)

## 🔹 Golang - It's survey time! How has Go has been working out for you?
The blog post discusses the annual Go user survey, encouraging Go developers to participate and share their experiences with the programming language. The survey aims to gather feedback to help improve Go and shape its future development. Participants have the opportunity to influence the direction of Go by providing insights into what works well and what could be improved. The post emphasizes the importance of community input in the evolution of Go.
👉 [Read more](https://go.dev/blog/survey2025-announce)

## 🔹 Helm - Path To Releasing Helm v4
The blog post discusses the release of the first Alpha version of Helm v4, marking a significant step in its development. As Helm v4 approaches its final stages, the post outlines ongoing activities and invites the community to participate in the process. The blog provides details on how enthusiasts and contributors can engage with the project to help shape the final release of Helm v4.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

