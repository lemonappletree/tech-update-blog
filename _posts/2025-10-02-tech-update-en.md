# 🛠️ 2025-10-02 Tech Update Summary

## 🔹 Kubernetes - Announcing Changed Block Tracking API support (alpha)
The blog post announces the alpha release of the Changed Block Tracking API, which enhances the Kubernetes storage ecosystem by allowing CSI storage drivers to efficiently identify changed blocks in PersistentVolume snapshots. This feature speeds up backup operations by focusing only on modified data instead of scanning entire volumes. The API supports block volumes but not file volumes and includes three key components: the CSI SnapshotMetadata Service API, a Kubernetes CustomResourceDefinition, and an External Snapshot Metadata Sidecar. Storage providers must implement CSI RPCs, have storage backend capabilities, and deploy external components to support this feature. Backup solutions must establish authentication, implement client-side streaming, and optimize workflows using the changed block metadata. The post also outlines how to get started with this feature, its benefits, and how to get involved in its development through the Kubernetes Storage Special Interest Group.
👉 [Read more](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/)

## 🔹 Spring Boot - Spring AI 1.0.3 Available Now
The Spring AI team has released version 1.0.3, now available from Maven Central. This patch update focuses on stability improvements and bug fixes, featuring 27 changes including 18 enhancements, 6 bug fixes, and 3 documentation updates. Key highlights include improvements in GemFire Vector Store, AWS Bedrock, GraalVM Native Image, Spring Bean Injection, and developer experience. The team is working towards a 1.1 GA release, focusing on Model Context Protocol functionality. Contributions and community engagement are encouraged through their GitHub repository and community channels.
👉 [Read more](https://spring.io/blog/2025/10/01/spring-ai-1-0-3-available-now)

## 🔹 Docker - Expanding Docker Hardened Images: Secure Helm Charts for Deployments
The blog post discusses the increasing need for development teams to secure their software supply chains, emphasizing the importance of trusted images, efficient deployments, and compliance-ready tools. It highlights that customers are seeking long-term security partners rather than one-off vendors. Docker responds to this demand by expanding its offerings to include Docker Hardened Images and Secure Helm Charts for deployments, aiming to provide more robust security solutions and foster greater trust and collaboration with its users.
👉 [Read more](https://www.docker.com/blog/docker-hardened-images-helm-charts-beta/)

## 🔹 Java - Oracle Java Extension for Visual Studio Code Version 24.1.2 Is Now Available!
The blog post announces the release of Oracle Java Extension version 24.1.2 for Visual Studio Code. This update brings new features and enhancements to the Java Platform Extension for VS Code, improving the development experience for Java developers using this popular code editor. For more details, readers are encouraged to visit the provided link.
👉 [Read more](https://inside.java/2025/10/01/java-vscode-extension-update/)

## 🔹 Golang - Flight Recorder in Go 1.25
The blog post discusses the introduction of a new diagnostic tool called "flight recording" in Go 1.25. This tool is designed to help developers by capturing detailed execution traces and system events. It aims to enhance the debugging and performance analysis of Go applications by providing a comprehensive view of the application's behavior over time. The post likely details how to use the flight recorder and its benefits in improving the development process.
👉 [Read more](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
The blog post announces the release of the first alpha version of Helm v4. As the development of Helm v4 approaches its final stages, the post provides details on the current progress and outlines how the wider community can participate and contribute to the process. The post aims to engage the community in the development of Helm v4 and encourages involvement from interested contributors.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

