# 🛠️ 2025-07-05 Tech Update Summary

## 🔹 Kubernetes - Navigating Failures in Pods With Devices
The blog post discusses the complexities of managing device failures in Kubernetes, particularly for AI/ML workloads that rely on specialized hardware like GPUs. It highlights challenges in handling device failures effectively due to Kubernetes's static view of resources and lack of robust support for hardware failures. The post outlines various failure modes, including infrastructure, device, container code, and device degradation failures, and presents DIY solutions and best practices for managing these issues. It emphasizes the need for Kubernetes to improve its handling of device failures through enhanced extension points and better failure information availability. The roadmap includes plans to address infrastructure reliability, integrate device failures into pod policies, and improve container code failure handling. While Kubernetes remains the preferred platform for AI/ML workloads due to its maturity and ecosystem, the blog encourages community involvement in enhancing device failure management.
👉 [Read more](https://kubernetes.io/blog/2025/07/03/navigating-failures-in-pods-with-devices/)

## 🔹 Spring Boot - Spring gRPC 0.9.0 available now
The blog post announces the release of Spring gRPC version 0.9.0, now available on Maven Central. Key updates in this release include an upgrade to Spring Boot 3.5, changes to the `StubFactory` contract making the "supports" method static, the removal of `GrpcClientFactoryCustomizer` in favor of `GrpcChannelBuilderCustomizer`, and new capabilities for filtering interceptors and service definitions in both in-process and Netty gRPC servers. The post also invites the community to contribute by checking open issues on GitHub and asks those with questions to use the `spring-grpc` tag on Stack Overflow. Links to GitHub, documentation, and Stack Overflow are provided for further engagement.
👉 [Read more](https://spring.io/blog/2025/07/04/spring-grpc-0-9-0-available-now)

## 🔹 Docker - 5 Best Practices for Building, Testing, and Packaging MCP Servers
The blog post discusses best practices for building, testing, and packaging MCP (Managed Container Platform) servers. It introduces a newly revamped Docker MCP Catalog, which enhances server discovery and simplifies the submission process. Containerized MCP servers are highlighted as a secure solution for running and scaling agentic applications while reducing risks associated with host access and secret management. Developers have two options for submitting servers: using Docker-built servers that include a comprehensive security suite, or through an alternative method not detailed in the summary.
👉 [Read more](https://www.docker.com/blog/mcp-server-best-practices/)

## 🔹 Java - Java 25 is ALSO no LTS Version - Inside Java Newscast #94
The blog post titled "Java 25 is ALSO no LTS Version - Inside Java Newscast #94" discusses the misconception around Java 25 being labeled as a "long-term-support (LTS) version." Similar to Java 21, this label is incorrect. The Java Community Process (JCP), which oversees the Java standard, and OpenJDK, responsible for the reference implementation, do not recognize the concept of "support" in their frameworks. The post explores the origins of this misunderstanding and its significance in the Java ecosystem.
👉 [Read more](https://inside.java/2025/07/03/newscast-94/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
The blog post discusses the Go programming team's plans for error handling support in the language. It explores the idea of introducing or not introducing syntactic support for error handling in Go. The team is considering various options and weighing the potential benefits and drawbacks. The goal is to improve error handling while maintaining Go's simplicity and effectiveness. The post outlines the current state of discussions and invites feedback from the community to help shape future developments in error handling for Go.
👉 [Read more](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The Helm team is attending KubeCon + CloudNativeCon EU 2025 in London from April 1-4. They will be discussing the upcoming release of Helm 4 and engaging with the community through talk sessions and their booth in the Project Pavilion. The blog post provides more details on the Helm-related activities planned for the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

