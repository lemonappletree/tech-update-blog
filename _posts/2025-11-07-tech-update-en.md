# 🛠️ 2025-11-07 Tech Update Summary

## 🔹 Kubernetes - Gateway API 1.4: New Features
The blog post discusses the release of Gateway API v1.4.0, which became generally available on October 6, 2025. This version introduces three new standard features: BackendTLSPolicy for TLS configuration between gateways and backends, the addition of the `supportedFeatures` field in GatewayClass status to declare supported features, and named rules for Routes to enhance observability and tooling. It also introduces three experimental features: a Mesh resource for service mesh configuration, default gateways to simplify configuration, and an `externalAuth` filter for HTTPRoute to enable external authentication services.

BackendTLSPolicy allows specifying TLS configuration for connections from Gateway to backend pods, improving security by enforcing encrypted traffic. The `supportedFeatures` field provides clarity on the capabilities of a GatewayClass, and named rules for Routes enhance status referencing, observability, and policy targeting.

Experimental features include the Mesh resource for mesh-wide settings and feature discovery, default gateways to ease the burden on developers by automatically selecting a gateway, and the `externalAuth` filter for calling external services to authenticate requests.

The release addresses a security vulnerability related to client certificate validation in connection reuse by introducing a per-port TLS configuration. This update allows for default and specific client certificate validation configurations, enhancing security across Listeners.

There are breaking changes, such as the requirement of the `.spec` field for GRPCRoute and stricter validation for the `allowCredentials` field in HTTPRoute's CORS policy. Efforts were made to improve the user and developer experience, including adding Kube API Linter to CI/CD pipelines and making documentation clearer about experimental features.

Users can try out the new version on Kubernetes 1.26 or later, with several implementations already conformant. The community is encouraged to get involved in shaping the future of Kubernetes routing APIs.
👉 [Read more](https://kubernetes.io/blog/2025/11/06/gateway-api-v1-4/)

## 🔹 Spring Boot - A Bootiful Podcast: The Vaadin team, live from Vaadin Create 2025
In this blog post, the author shares their experience of recording a podcast episode with notable figures from the Vaadin team: Joonas Lehtinen, Marcus Hellberg, and Leif Åstrand. The conversation took place at the Vaadin Create 2025 event in Frankfurt, Germany. The post highlights the insights and discussions shared during the podcast, focusing on the latest developments and innovations from the Vaadin team.
👉 [Read more](https://spring.io/blog/2025/11/06/a-bootiful-podcasd-vaadin-team)

## 🔹 Docker - Dynamic MCPs with Docker: Stop Hardcoding Your Agents’ World
The blog post discusses the evolution of the MCP (Micro Container Protocol) protocol, which is nearing its first anniversary. In the past year, developers have significantly expanded the MCP ecosystem, moving from using a few local MCP servers to having access to thousands. This growth has been facilitated by Docker, which allows for dynamic MCPs, eliminating the need to hardcode agents' environments. This development enables greater flexibility and scalability in deploying and managing MCP servers and tools.
👉 [Read more](https://www.docker.com/blog/dynamic-mcps-stop-hardcoding-your-agents-world/)

## 🔹 Java - Try the New Valhalla EA Build - Inside Java Newscast #100
The blog post discusses the recent re-entry of JEP 401, Value Classes and Objects, into "candidate" status as it prepares for a future release. To facilitate experimentation with identity-less value classes, Project Valhalla has released a new early-access build. These value classes offer benefits in code readability and maintenance, where applicable, and provide the Java runtime with opportunities for optimizations such as scalarization and heap flattening, with more enhancements expected in the future.
👉 [Read more](https://inside.java/2025/11/06/newscast-100/)

## 🔹 Golang - The Green Tea Garbage Collector
The blog post discusses the introduction of a new experimental garbage collector named Green Tea in Go version 1.25. This new garbage collector aims to improve memory management and performance by optimizing the way unused memory is reclaimed. The Green Tea garbage collector is designed to enhance the efficiency of Go applications, potentially leading to faster execution and reduced latency. While it is still experimental, developers can try it out and provide feedback to help refine its functionality for future versions.
👉 [Read more](https://go.dev/blog/greenteagc)

