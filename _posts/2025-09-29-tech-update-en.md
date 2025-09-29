# 🛠️ 2025-09-29 Tech Update Summary

## 🔹 Kubernetes - Announcing Changed Block Tracking API support (alpha)
The blog post announces the alpha release of the Changed Block Tracking API, which enhances Kubernetes' storage ecosystem. This feature enables more efficient backup operations by allowing CSI storage drivers to identify changed blocks in PersistentVolume snapshots. The API focuses on block-level changes, reducing the need to scan entire volumes during backups, and is currently supported only for block volumes, not file volumes. It aims to address challenges like long backup windows, high resource utilization, and increased storage costs. The implementation involves components such as the CSI SnapshotMetadata Service API, a Kubernetes CustomResourceDefinition, and an external snapshot metadata sidecar. Storage providers looking to integrate this feature must implement specific requirements, while backup solutions must handle authentication and optimize backup workflows. The blog suggests ways to get started with the feature, outlines future plans, and provides resources for further learning and community involvement.
👉 [Read more](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring Batch lead Mahmoud Ben Hassine
The blog post is about a podcast episode where the host talks with Mahmoud Ben Hassine, the lead of the Spring Batch project. They discuss the newest features and updates in Spring Batch as part of the Spring Boot 4 generation.
👉 [Read more](https://spring.io/blog/2025/09/25/a-bootiful-podcast-mahmoud-ben-hassine)

## 🔹 Docker - The Trust Paradox: When Your AI Gets Catfished
The blog post titled "The Trust Paradox: When Your AI Gets Catfished" discusses the vulnerabilities of AI systems to MCP-enabled attacks, which exploit the inherent trust within development teams. These attacks are not necessarily technically advanced but are effective because they manipulate the trust relationships that are essential for team functionality. For instance, designers and DevOps teams may expect and trust files and information from long-term collaborators, which attackers can exploit to deceive AI systems.
👉 [Read more](https://www.docker.com/blog/mcp-prompt-injection-trust-paradox/)

## 🔹 Java - Episode 40 “Amber &amp; Valhalla - Incremental Design and Feature Arcs” with Brian Goetz
In this episode of a tech podcast, Nicolai Parlog talks with Brian Goetz, the Java Language Architect at Oracle, about Project Amber and Project Valhalla. Brian provides insights and updates on these significant Java initiatives. The discussion includes Amber's upcoming feature arc and Valhalla's plans for null-restriction, among other topics.
👉 [Read more](https://inside.java/2025/09/28/podcast-040/)

## 🔹 Golang - Flight Recorder in Go 1.25
The blog post discusses the introduction of a new tool in Go 1.25 called "flight recording." This tool is added to the diagnostic toolbox in Go, providing developers with enhanced capabilities for monitoring and analyzing the behavior of Go programs. Flight recording is designed to capture detailed runtime information, which can help in diagnosing performance issues and understanding program execution. The feature aims to improve the overall efficiency and reliability of Go applications by allowing developers to gain insights into the runtime environment.
👉 [Read more](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
The blog post discusses the release of the first Alpha version of Helm v4, signaling that the development of this new version is nearing completion. It provides insights into the current development status and outlines how the broader community can participate and contribute to the process. The post aims to engage the community by sharing detailed information about the progress and upcoming features of Helm v4.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

