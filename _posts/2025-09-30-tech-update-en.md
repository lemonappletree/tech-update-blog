# 🛠️ 2025-09-30 Tech Update Summary

## 🔹 Kubernetes - Announcing Changed Block Tracking API support (alpha)
The blog post announces the alpha support for the Changed Block Tracking API in Kubernetes. This feature allows CSI storage drivers to efficiently identify changed blocks in PersistentVolume snapshots, leading to faster and more resource-efficient backup operations. Changed block tracking helps storage systems track modifications at the block level between snapshots, improving backup efficiency by focusing only on changed data blocks. Currently, this API supports only block volumes, not file volumes. The implementation includes three main components: the CSI SnapshotMetadata Service API, the SnapshotMetadataService API, and the External Snapshot Metadata Sidecar. Storage providers and backup solutions must meet specific requirements to support this feature. The post also outlines the benefits of this API, like reduced backup windows, lower resource utilization, and decreased storage costs. The Kubernetes team plans to advance this feature to Beta in future releases based on feedback and adoption. For more information, readers are directed to official documentation and related GitHub repositories. The post also invites contributors to join the Kubernetes Storage Special Interest Group for further involvement.
👉 [Read more](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring Batch lead Mahmoud Ben Hassine
In this tech blog post titled "A Bootiful Podcast: Spring Batch lead Mahmoud Ben Hassine," the host talks to Mahmoud Ben Hassine, the lead of the Spring Batch project. The discussion focuses on the latest developments and enhancements in the Spring Batch framework within the context of the upcoming Spring Boot 4 generation.
👉 [Read more](https://spring.io/blog/2025/09/25/a-bootiful-podcast-mahmoud-ben-hassine)

## 🔹 Docker - Expanding Docker Hardened Images: Secure Helm Charts for Deployments
The blog post discusses the increasing demand for secure software supply chains among development teams. These teams require trusted images, efficient deployment processes, and tools that are compliant with regulations, provided by reliable long-term partners. In response, Docker is expanding its offering by introducing Docker Hardened Images and secure Helm Charts for deployments. This initiative aims to address the needs of customers who are seeking comprehensive security partnerships throughout the development and deployment phases, rather than relying on one-off vendors.
👉 [Read more](https://www.docker.com/blog/docker-hardened-images-helm-charts-beta/)

## 🔹 Java - Episode 40 “Amber &amp; Valhalla - Incremental Design and Feature Arcs” with Brian Goetz
In episode 40 of the tech podcast, Nicolai Parlog converses with Brian Goetz, Java Language Architect at Oracle and head of Project Amber and Project Valhalla. The discussion focuses on the latest developments and updates related to these projects. They explore the forthcoming feature arc for Project Amber and discuss the planned null-restriction in Project Valhalla, among other topics.
👉 [Read more](https://inside.java/2025/09/28/podcast-040/)

## 🔹 Golang - Flight Recorder in Go 1.25
The blog post discusses the introduction of a new diagnostic tool called "flight recording" in Go 1.25. This tool is designed to help developers capture detailed runtime information about their applications, which can be used for performance analysis and debugging. The flight recorder continuously records data and allows developers to retrieve snapshots of the program's execution, making it easier to identify and resolve issues. The post highlights the benefits of this new feature and provides insights into how it can enhance the development and maintenance of Go applications.
👉 [Read more](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
The blog post discusses the release of the first alpha version of Helm v4, marking a significant milestone as it nears completion. It provides details about the ongoing development process and encourages the community to participate and contribute. The post aims to engage the broader community by providing insights into the new version's features and how individuals can get involved in its development. For more information, readers are directed to the full post on the Helm website.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

