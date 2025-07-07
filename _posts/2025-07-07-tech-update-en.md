# 🛠️ 2025-07-07 Tech Update Summary

## 🔹 Kubernetes - Navigating Failures in Pods With Devices
The blog post discusses the complexities of managing failures in Kubernetes pods that utilize specialized hardware like GPUs, especially in the context of AI/ML workloads. It highlights the challenges posed by the static nature of Kubernetes' resource management, which doesn't adequately handle hardware failures or degradation. The post outlines various failure modes, including infrastructure-related issues, device failures, and container code failures, and examines DIY solutions currently used to mitigate these problems. Despite these challenges, Kubernetes remains the preferred platform for AI/ML workloads due to its maturity and robust ecosystem. The blog also details a roadmap for improving Kubernetes' handling of device failures, emphasizing the need for better extension points and error handling mechanisms. The Kubernetes community is encouraged to participate in discussions and contribute to the development of more effective solutions for managing device failures.
👉 [Read more](https://kubernetes.io/blog/2025/07/03/navigating-failures-in-pods-with-devices/)

## 🔹 Spring Boot - Spring gRPC 0.9.0 available now
The blog post announces the release of Spring gRPC 0.9.0, which is now available on Maven Central. The release includes several updates such as an upgrade to Spring Boot 3.5, changes to the `StubFactory` contract with the "supports" method now being static, and the removal of `GrpcClientFactoryCustomizer` in favor of `GrpcChannelBuilderCustomizer`. It also adds features for filtering interceptors in in-process gRPC clients and filtering global interceptors and service definitions. The post invites contributions and questions, directing interested individuals to GitHub for issues and Stack Overflow for general inquiries.
👉 [Read more](https://spring.io/blog/2025/07/04/spring-grpc-0-9-0-available-now)

## 🔹 Docker - 5 Best Practices for Building, Testing, and Packaging MCP Servers
The blog post discusses best practices for building, testing, and packaging MCP (Managed Container Platform) servers. It highlights the launch of a revamped Docker MCP Catalog that enhances discovery and introduces a new submission process. The post emphasizes the benefits of containerized MCP servers, such as providing a secure environment for running and scaling agentic applications while reducing risks associated with host access and secret management. Developers have two options for submitting servers: using Docker-built servers that come with a comprehensive security suite, or another unspecified method.
👉 [Read more](https://www.docker.com/blog/mcp-server-best-practices/)

## 🔹 Java - Java 25 is ALSO no LTS Version - Inside Java Newscast #94
In the blog post titled "Java 25 is ALSO no LTS Version - Inside Java Newscast #94," the author clarifies that labeling Java 25 as a "long-term-support (LTS) version" is incorrect, similar to the miscategorization of Java 21. The post explains that neither the Java Community Process (JCP), which oversees Java standards, nor OpenJDK, which develops the reference implementation, recognize the concept of "support" in their frameworks. The post delves into the origins of this misconception and discusses its significance in the context of Java development and versioning.
👉 [Read more](https://inside.java/2025/07/03/newscast-94/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
The blog post discusses the Go programming language team's plans regarding syntactic support for error handling. It explores potential changes and improvements to how error handling is implemented in Go, weighing the pros and cons of different approaches. The goal is to enhance the language's usability and maintainability while considering the needs of the Go community. The post emphasizes the team's commitment to thoughtful, community-informed decisions in the evolution of Go's error handling capabilities.
👉 [Read more](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The Helm team is attending KubeCon + CloudNativeCon EU 2025 in London from April 1st to 4th. With Helm 4 set to be released later this year, the team invites attendees to engage in discussions with maintainers during talk sessions and visit their booth in the Project Pavilion. The blog post provides further details on Helm-related activities throughout the event week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

