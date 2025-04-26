# 🛠️ 2025-04-26 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: User Namespaces enabled by default!
The blog post discusses the release of Kubernetes v1.33, which now has user namespaces enabled by default. This feature allows pods to use user namespaces without needing to enable a Kubernetes feature flag. User namespaces isolate UIDs and GIDs in containers from those on the host, preventing lateral movement, increasing host isolation, and enabling new use cases. The post explains the significance of user namespaces, how to configure them, and the requirements for using them, such as kernel support for idmap mounts. It also addresses common questions and provides resources for further learning. The post concludes by highlighting the benefits of user namespaces in running pods securely and encourages involvement with the Kubernetes community.
👉 [Read more](https://kubernetes.io/blog/2025/04/25/userns-enabled-by-default/)

## 🔹 Spring Boot - Spring Boot 3.5.0-RC1 available now
The tech blog post announces the release of Spring Boot 3.5.0-RC1, which is now available for download. This version includes 133 enhancements, documentation improvements, dependency upgrades, and bug fixes. Notable features in this release are support for Docker's credential stores and helpers, improved configuration property binding performance, annotation-based filter and servlet registration, auto-configuration for background initialization of beans, and properties for global WebClient configuration. The post provides links to the release notes for more details and encourages community contributions, highlighting the "ideal for contribution" tag in the issue repository for those interested in helping. Additional resources such as the project page, GitHub, documentation, and Stack Overflow links are also provided for further engagement and support.
👉 [Read more](https://spring.io/blog/2025/04/25/spring-boot-3-5-0-RC1-available-now)

## 🔹 Docker - How to build and deliver an MCP server for production
The blog post discusses the process of building and deploying a Model Context Protocol (MCP) server for production. Initially introduced in December 2024 in collaboration with Anthropic, MCP is a specification designed to run tools with AI agents. Since its release, there has been significant interest from developers in creating, sharing, and utilizing their tools with Agentic AI using MCP. The blog provides insights and guidance on leveraging Docker to efficiently build and deliver MCP servers in a production environment.
👉 [Read more](https://www.docker.com/blog/build-to-prod-mcp-servers-with-docker/)

## 🔹 Java - Finalizing the Java On-ramp - Inside Java Newscast #90
The blog post discusses upcoming changes in Java 25, specifically focusing on the finalization of the "Paving the On-ramp" feature set. This new feature aims to improve accessibility and user-friendliness for Java developers. Additionally, the post announces the launch of a new website, lear.java, which is designed to assist both learners and educators in writing and teaching Java.
👉 [Read more](https://inside.java/2025/04/24/ijn-ep-90/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
The blog post discusses improvements in benchmark looping introduced in Go 1.24 through the `testing.B.Loop` feature. This enhancement aims to make benchmarking more predictable and reliable by providing a more consistent way to control iteration loops during tests. The update is designed to help developers achieve more accurate performance measurements in their code by minimizing variance and improving the precision of benchmarking results.
👉 [Read more](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces the Helm team's participation in KubeCon + CloudNativeCon EU 2025, taking place in London from April 1 to 4. The team is excited to discuss the upcoming release of Helm 4 and invites attendees to engage with them during talk sessions and at the Helm booth in the Project Pavilion. The post encourages participants to join the conversation and provides details on all Helm-related activities during the conference.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

