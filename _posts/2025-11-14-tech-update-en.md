# 🛠️ 2025-11-14 Tech Update Summary

## 🔹 Kubernetes - Ingress NGINX Retirement: What You Need to Know
The blog post announces the upcoming retirement of Ingress NGINX by Kubernetes SIG Network and the Security Response Committee, aimed at prioritizing ecosystem safety and security. Best-effort maintenance will continue until March 2026, after which no further releases, bug fixes, or security updates will be provided. While existing deployments will remain functional, users are advised to migrate to alternatives like the Gateway API or other Ingress controllers. The post highlights the history and challenges of maintaining Ingress NGINX, noting its popularity and the maintenance struggles due to limited personnel. Current users are urged to plan migrations immediately to ensure continued security and functionality.
👉 [Read more](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)

## 🔹 Spring Boot - Spring Cloud 2025.1.0-RC1 (aka Oakwood) has been released
The blog post announces the release of Spring Cloud 2025.1.0-RC1, also known as Oakwood. This release, available in the Spring Milestone repository, includes support for Spring Boot 4.0.0-RC2, updates for Jackson 3, initial support for JSpecify Null-Safety, and various dependency updates and bug fixes. Key changes involve enhancements across several Spring Cloud projects, such as Spring Cloud Function, Consul, Gateway, Commons, Vault, Stream, Config, Contract, Kubernetes, and Circuitbreaker. Notable improvements include null-safety annotations, migration to Jackson 3, support for complex input/output types in Spring Cloud Function, and a new resilience module in Spring Cloud Circuitbreaker. The release encourages community feedback and provides guidance on integrating the update with Maven and Gradle.
👉 [Read more](https://spring.io/blog/2025/11/13/spring-cloud-2025-1-0-RC1-aka-oakwood-has-been-released)

## 🔹 Docker - Cagent Comes to Docker Desktop with Built-In IDE Support through ACP
Docker Desktop has integrated cagent, an open-source tool by Docker, directly into its platform, allowing developers to build AI agents without needing a separate installation. Cagent enables users to create AI agents using YAML configuration files, eliminating the need for coding. This integration simplifies the process of defining agent behavior and tools, streamlining AI development for Docker Desktop users.
👉 [Read more](https://www.docker.com/blog/cagent-comes-to-docker-desktop-with-built-in-ide-support-through-acp/)

## 🔹 Java - JEP targeted to JDK 26: 516: Ahead-of-Time Object Caching with Any GC
The blog post discusses JEP 516, which is aimed for inclusion in JDK 26. This proposal focuses on implementing Ahead-of-Time (AOT) Object Caching that can work with any Garbage Collector (GC). The goal is to enhance Java's performance by allowing objects to be cached ahead of time, potentially improving startup times and overall efficiency. The JEP is designed to be compatible with various garbage collection strategies, making it versatile for different use cases. This improvement is expected to be part of the upcoming JDK 26 release.
👉 [Read more](https://inside.java/2025/11/13/jep516-target-jdk26/)

## 🔹 Golang - The Green Tea Garbage Collector
The blog post discusses the introduction of a new experimental garbage collector called Green Tea in Go version 1.25. This new garbage collector aims to improve memory management by optimizing performance and reducing latency in Go applications. The Green Tea garbage collector is part of ongoing efforts to enhance the efficiency of Go's runtime system. The post provides an overview of how the Green Tea garbage collector works and its potential benefits for developers using Go.
👉 [Read more](https://go.dev/blog/greenteagc)

