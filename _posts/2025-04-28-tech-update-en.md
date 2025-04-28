# 🛠️ 2025-04-28 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: User Namespaces enabled by default!
The blog post announces that in Kubernetes v1.33, support for user namespaces is enabled by default, allowing pods to use user namespaces without needing to enable any feature flag. User namespaces are a Linux kernel feature that isolates UIDs and GIDs of containers from the host, offering benefits such as preventing lateral movement, increasing host isolation, and enabling new use cases without granting root access. The post explains how to configure pods to use user namespaces and discusses the importance of idmap mounts in supporting file systems used by pods. It also addresses common questions about requirements, configuration, and the impact of user namespaces on security, demonstrated by mitigating certain CVEs. The post encourages users to try user namespaces for enhanced security and provides resources for further learning and community involvement.
👉 [Read more](https://kubernetes.io/blog/2025/04/25/userns-enabled-by-default/)

## 🔹 Spring Boot - Spring Boot 3.5.0-RC1 available now
The blog post announces the release of Spring Boot 3.5.0-RC1, which is now available for download. This release includes 133 improvements, such as enhancements, documentation updates, dependency upgrades, and bug fixes. Key new features are support for Docker's credential stores with Cloud Native Buildpacks, improved configuration property binding performance, annotation-based filter and servlet registration, auto-configuration for bean background initialization, and global WebClient configuration properties. Readers are encouraged to view the release notes for detailed information and upgrade instructions. The post thanks contributors and provides guidance for those interested in contributing to the project. Links to the project page, GitHub, issues, documentation, and Stack Overflow are also provided.
👉 [Read more](https://spring.io/blog/2025/04/25/spring-boot-3-5-0-RC1-available-now)

## 🔹 Docker - How to build and deliver an MCP server for production
The blog post discusses the growing interest in using the Model Context Protocol (MCP) to run tools with AI agents, following its introduction in December 2024 by Anthropic. It highlights the surge in developers' enthusiasm for building, sharing, and running tools with Agentic AI using MCP. The post outlines how to build and deploy an MCP server for production, leveraging Docker, and provides insights into the benefits and applications of using MCP in AI tool development.
👉 [Read more](https://www.docker.com/blog/build-to-prod-mcp-servers-with-docker/)

## 🔹 Java - Finalizing the Java On-ramp - Inside Java Newscast #90
The blog post discusses significant updates coming to Java in the Java 25 release, particularly focusing on the finalization of the "Paving the On-ramp" feature set. Additionally, the post highlights the launch of a new website, lear.java, which is designed for individuals interested in learning Java and educators teaching the language. This episode of the Inside Java Newscast provides insights into these developments.
👉 [Read more](https://inside.java/2025/04/24/ijn-ep-90/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
The blog post discusses improvements in benchmarking within the Go programming language, specifically focusing on the introduction of `testing.B.Loop` in Go 1.24. This new feature aims to make benchmark loops more predictable and consistent by providing a structured way to run benchmarks. It enhances the accuracy of performance measurements and helps developers achieve more reliable results when testing their code's efficiency. The post likely provides insights into how this feature works, its benefits, and possibly examples of its implementation for developers working with Go.
👉 [Read more](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces the Helm team's participation in KubeCon + CloudNativeCon EU 2025, which will take place in London, UK, from April 1-4. The team will discuss the upcoming release of Helm 4 and invites attendees to engage with maintainers during talk sessions and at the Helm booth in the Project Pavilion. The post includes details on various Helm-related activities throughout the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

