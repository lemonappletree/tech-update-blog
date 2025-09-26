# 🛠️ 2025-09-26 Tech Update Summary

## 🔹 Kubernetes - Announcing Changed Block Tracking API support (alpha)
The blog post announces the alpha release of the Changed Block Tracking API, which enhances the Kubernetes storage ecosystem. This feature allows CSI storage drivers to efficiently identify changed blocks in PersistentVolume snapshots, leading to faster and more resource-efficient backup operations. Changed block tracking improves backup processes by tracking modifications at the block level, eliminating the need to scan entire volumes. This API is currently supported for block volumes but not for file volumes. The implementation includes three main components: the CSI SnapshotMetadata Service API, the SnapshotMetadataService API, and the External Snapshot Metadata Sidecar. Storage providers must implement specific requirements to support this feature, and backup solutions need to set up proper authentication and client-side code. The post also outlines the benefits of this feature, including reduced backup duration and resource consumption. The blog encourages interested users to try the feature and provides resources for learning more and contributing to the project.
👉 [Read more](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring Batch lead Mahmoud Ben Hassine
The blog post is about a podcast episode where the host talks with Mahmoud Ben Hassine, the lead of the Spring Batch project. They discuss the newest features and updates in Spring Batch as part of the Spring Boot 4 generation.
👉 [Read more](https://spring.io/blog/2025/09/25/a-bootiful-podcast-mahmoud-ben-hassine)

## 🔹 Docker - Introducing the Docker Premium Support and TAM service
The blog post announces the launch of Docker's new Premium Support and Technical Account Management (TAM) service. This service is intended to provide enhanced support for Docker's customers, including 24/7 availability, priority service-level agreements (SLAs), expert guidance, and additional TAM services. These offerings are specifically designed to support developers and global businesses, ensuring they have the necessary resources and assistance to succeed.
👉 [Read more](https://www.docker.com/blog/introducing-the-docker-premium-support-and-tam-service/)

## 🔹 Java - Reviewing the JDK 25 Release Notes - Inside Java Newscast #98
The blog post discusses the JDK 25 release notes as covered in episode 98 of the Inside Java Newscast. JDK 25 is significant because it offers long-term support (LTS), prompting many Java developers to consider migrating to it eventually. The episode provides a comprehensive review of the release notes, highlighting all the significant changes and updates in this latest version of the Java Development Kit.
👉 [Read more](https://inside.java/2025/09/25/newscast-98/)

## 🔹 Golang - It's survey time! How has Go has been working out for you?
The blog post announces a survey for Go programming language users, inviting them to share their experiences and feedback. The aim is to gather insights from the community to guide the future development of Go. Participants' input will help the Go team understand how the language is being used and identify areas for improvement. The post encourages users to take part in shaping the future of Go by contributing their thoughts through the survey.
👉 [Read more](https://go.dev/blog/survey2025-announce)

## 🔹 Helm - Path To Releasing Helm v4
The blog post announces the release of the first Alpha version of Helm v4, marking a significant milestone in its development. It details the current progress and outlines how the development is nearing completion. The post also invites the broader community to engage and participate in the development process, providing insights into upcoming features and changes. The link to the full blog post is provided for readers who want more detailed information.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

