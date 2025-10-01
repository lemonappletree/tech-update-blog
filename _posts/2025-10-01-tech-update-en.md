# 🛠️ 2025-10-01 Tech Update Summary

## 🔹 Kubernetes - Announcing Changed Block Tracking API support (alpha)
The blog post announces the alpha support for a Changed Block Tracking API in Kubernetes, which enhances the storage ecosystem by allowing CSI storage drivers to efficiently identify changed blocks in PersistentVolume snapshots. This feature enables faster and more resource-efficient backup operations by tracking modifications at the block level, eliminating the need to scan entire volumes during backups. It is currently supported only for block volumes, not file volumes. The implementation involves key components like the CSI SnapshotMetadata Service API, SnapshotMetadataService API, and the External Snapshot Metadata Sidecar. Storage providers and backup solutions need to implement specific requirements to leverage this feature. The post also details the benefits of this API, such as reducing backup windows, resource utilization, and storage costs. It provides guidance on getting started with the feature and discusses its potential future developments. Interested users can find more information through the provided links to official documentation and GitHub repositories. The post acknowledges contributors who helped in the design and implementation and encourages participation in the Kubernetes Storage Special Interest Group.
👉 [Read more](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/)

## 🔹 Spring Boot - Securing MCP Servers with Spring AI
The tech blog post discusses securing Model Context Protocol (MCP) servers using Spring AI. It highlights the evolving security aspects of MCP and introduces a dedicated project on GitHub, `spring-ai-community/mcp-security`, which is now available for Spring AI 1.1.x-based applications. The post covers three main topics: securing MCP servers with OAuth2, building an MCP-compatible Spring Authorization Server, and using API keys as an alternative to OAuth2.

For OAuth2, the blog explains how to secure MCP servers using OAuth2 access tokens, requiring configuration with a trusted authorization server. It provides detailed instructions on setting up dependencies, configuration, and a sample greeting tool to demonstrate user authentication.

For building an MCP-compatible Spring Authorization Server, it guides readers on creating a server using Spring Authorization Server and configuring clients and users.

The post also addresses environments that lack OAuth2 infrastructure by supporting API keys for authentication. It provides examples of configuring API key security in a Spring application.

Finally, the blog encourages readers to explore the `mcp-security` project for more documentation and samples, inviting contributions and feedback.
👉 [Read more](https://spring.io/blog/2025/09/30/spring-ai-mcp-server-security)

## 🔹 Docker - Expanding Docker Hardened Images: Secure Helm Charts for Deployments
The blog post discusses the importance of securing software supply chains for development teams and the growing need for trusted images and compliant tooling. Customers are seeking long-term security partners for both development and deployment rather than one-off vendors. In response, Docker is expanding its offerings to include hardened images and secure Helm charts to streamline deployments and enhance security. This initiative aims to provide development teams with the reliable tools and partnerships necessary for maintaining a secure and efficient software supply chain.
👉 [Read more](https://www.docker.com/blog/docker-hardened-images-helm-charts-beta/)

## 🔹 Java - Episode 40 “Amber &amp; Valhalla - Incremental Design and Feature Arcs” with Brian Goetz
In episode 40 of the podcast, Nicolai Parlog talks with Brian Goetz, the Java Language Architect at Oracle. They discuss updates on Project Amber and Project Valhalla, two significant initiatives in the Java community. Brian Goetz provides insights into Amber's upcoming feature arc and Valhalla's plans for implementing null-restriction, among other topics.
👉 [Read more](https://inside.java/2025/09/28/podcast-040/)

## 🔹 Golang - Flight Recorder in Go 1.25
The blog post discusses the introduction of a new diagnostic tool called "flight recording" in Go 1.25. This tool aims to enhance the ability to diagnose and troubleshoot issues by providing a way to record and analyze the execution of Go programs. It is designed to help developers gain insights into program behavior and performance by capturing detailed runtime information. The post explains the benefits of this feature, how it can be utilized, and its impact on improving the overall development and debugging experience in Go.
👉 [Read more](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
The blog post titled "Path To Releasing Helm v4" announces the release of the first Alpha version for Helm v4. It explains that the development of Helm v4 is nearing completion and provides details on the ongoing processes. The post also outlines ways for the broader community to get involved with the development and contribute to the final release of Helm v4. For more information, readers are directed to the full blog post on the Helm website.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

