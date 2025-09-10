# 🛠️ 2025-09-10 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.34: Snapshottable API server cache
The blog post discusses the enhancements introduced in Kubernetes v1.34, focusing on the "snapshottable API server cache" feature, which has progressed to Beta. This feature is part of a broader effort to improve API server stability and performance by mitigating memory usage and load on the etcd datastore. Key improvements in previous releases included consistent reads from the cache (Beta in v1.31) and streaming large responses (Beta in v1.33). The new feature allows for efficient, point-in-time snapshots of the cache, enabling almost all read requests to be served from memory, reducing memory pressure, and stabilizing the control plane. The "SnapshottableCache" feature gate is enabled by default in Kubernetes v1.34, requiring no user action to leverage these improvements. Acknowledgments are given to various contributors from different organizations for their roles in implementing these features.
👉 [Read more](https://kubernetes.io/blog/2025/09/09/kubernetes-v1-34-snapshottable-api-server-cache/)

## 🔹 Spring Boot - Access API Moves to Spring Security Access
The blog post discusses the transition of Spring Security's authorization API over the past five years, leading to new features like Authorized POJOs, value masking, and planned Multi-Factor Authentication in Spring Security 7. The transition deprecated most of the Access API components, such as AccessDecisionManager and FilterSecurityInterceptor, along with @EnableGlobalMethodSecurity. To aid organizations in migrating, Spring Security 7.0.0-M3 introduces an optional module, spring-security-access, containing the deprecated components. This module is necessary only for applications still using the old Access API components. For those already using AuthorizationManager, no changes are needed. The post provides migration hints to help with the transition.
👉 [Read more](https://spring.io/blog/2025/09/09/access-api-moves-to-spring-security-access)

## 🔹 Docker - Docker Acquisition of MCP Defender Helps Meet Challenges of Securing the Agentic Future
Docker, Inc., a company known for providing cloud-native and AI-native development tools and services, has announced its acquisition of MCP Defender. MCP Defender is a company focused on securing AI applications. This acquisition addresses the growing challenges in securing AI as it evolves from basic generative models to more advanced, agentic tools, which are significantly transforming software development. While these powerful technologies offer new capabilities, they also introduce new security challenges that Docker aims to tackle with this acquisition.
👉 [Read more](https://www.docker.com/blog/docker-acquires-mcp-defender-ai-agent-security/)

## 🔹 Java - All API Additions From Java 21 to 25 #RoadTo25
The blog post titled "All API Additions From Java 21 to 25 #RoadTo25" provides a comprehensive overview of the new API features introduced between Java versions 21 and 25. Key additions include scoped values, which help manage state more effectively; stream gatherers for enhanced data processing; a class-file API for better manipulation of class files; and a foreign function and memory API that facilitates interaction with non-Java code and memory. Additionally, there are enhancements to Javadoc to improve documentation capabilities. The post serves as a guide for developers to understand and leverage these new features in their projects.
👉 [Read more](https://inside.java/2025/09/09/roadto25-api/)

## 🔹 Golang - A new experimental Go API for JSON
The tech blog post discusses the introduction of experimental support in Go 1.25 for two new packages: `encoding/json/jsontext` and `encoding/json/v2`. These packages aim to provide improved handling and flexibility for working with JSON data in the Go programming language. The post likely elaborates on the features, potential benefits, and possibly the motivations behind this development. For more detailed information, readers are encouraged to visit the provided link to the original blog post on the Go website.
👉 [Read more](https://go.dev/blog/jsonv2-exp)

## 🔹 Helm - Path To Releasing Helm v4
The blog post discusses the release of the first Alpha version of Helm v4, indicating that the development of this new version is nearing completion. It provides details on the current status of the project and outlines ways for the broader community to participate and contribute to the final stages of Helm v4's development.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

