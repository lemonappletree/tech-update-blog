# 🛠️ 2025-04-27 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: User Namespaces enabled by default!
The blog post announces that Kubernetes v1.33 has enabled user namespaces by default, allowing pods to opt-in to use them without needing to enable any feature flags. User namespaces, distinct from Kubernetes namespaces, are a Linux kernel feature that isolates UIDs and GIDs of containers from the host, offering enhanced security and enabling certain capabilities within the container without host privileges. This isolation prevents lateral movement between containers and increases host isolation, while also allowing new use cases like running applications requiring privileged operations securely. The post addresses common questions about user namespaces, including configuration, requirements, and the concept of idmap mounts. It highlights the importance of user namespaces in improving security without application changes and notes their support in container runtimes like containerd and CRI-O. The post concludes by encouraging engagement with the Kubernetes community and provides resources for further learning.
👉 [Read more](https://kubernetes.io/blog/2025/04/25/userns-enabled-by-default/)

## 🔹 Spring Boot - Spring Boot 3.5.0-RC1 available now
The blog post announces the release of Spring Boot 3.5.0-RC1, which is now available for download. This release includes 133 enhancements, documentation improvements, dependency upgrades, and bug fixes. Notable new features include support for Docker's credential stores and helpers, improved configuration property binding performance, annotation-based filter and servlet registration, auto-configuration for background initialization of beans, and properties for global WebClient configuration. The post thanks contributors and provides links to release notes, upgrade instructions, and ways to contribute. For questions, users are directed to Stack Overflow with the "spring-boot" tag. The blog also provides links to the project page, GitHub repository, issues page, documentation, and Stack Overflow for further resources.
👉 [Read more](https://spring.io/blog/2025/04/25/spring-boot-3-5-0-RC1-available-now)

## 🔹 Docker - How to build and deliver an MCP server for production
The blog post discusses the development and deployment of a Model Context Protocol (MCP) server for production, a concept introduced in collaboration with Anthropic in December 2024. The MCP allows for the integration and operation of tools using AI agents. Since its introduction, there has been a significant increase in developer interest in creating, sharing, and utilizing tools with Agentic AI, all facilitated by MCP. The post likely provides insights into the technical aspects and benefits of implementing MCP servers, possibly using Docker for building and deployment.
👉 [Read more](https://www.docker.com/blog/build-to-prod-mcp-servers-with-docker/)

## 🔹 Java - Finalizing the Java On-ramp - Inside Java Newscast #90
The blog post discusses upcoming changes in the Java 25 release, focusing on the finalization of the "Paving the On-ramp" feature set. This new feature aims to make Java more accessible and easier to learn for beginners. Additionally, the post introduces a new website, lear.java, which is dedicated to helping people learn Java and assisting educators in teaching the language.
👉 [Read more](https://inside.java/2025/04/24/ijn-ep-90/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
The blog post discusses improvements in benchmark looping introduced in Go 1.24 through the `testing.B.Loop` function. This new feature aims to provide more predictable and consistent benchmarking results by refining how loops are handled during testing. The update helps developers achieve more accurate performance measurements, enhancing the reliability of benchmarking in Go programming.
👉 [Read more](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces the Helm team's participation in the KubeCon + CloudNativeCon EU '25 event in London from April 1-4. The team will discuss the upcoming Helm 4 release and engage with attendees during talk sessions and at their booth in the Project Pavilion. The post invites readers to join the conversation with Helm maintainers and provides details on Helm-related activities throughout the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

