# 🛠️ 2025-09-28 Tech Update Summary

## 🔹 Kubernetes - Announcing Changed Block Tracking API support (alpha)
The blog post announces the alpha support for the Changed Block Tracking API in Kubernetes, which is designed to enhance the Kubernetes storage ecosystem by allowing CSI storage drivers to efficiently identify changed blocks in PersistentVolume snapshots. This feature aims to streamline backup operations by focusing only on the changed data blocks, thus making backups faster and more resource-efficient. The Changed Block Tracking API is currently supported only for block volumes and not for file volumes. The post details the components and implementation requirements for storage providers and backup solutions to leverage this feature, along with instructions for getting started with it. Additionally, the post discusses the potential benefits of the API, such as reducing backup duration, resource consumption, and storage costs. The blog encourages feedback and participation from the community to help advance the feature from alpha to beta in future releases. It provides links to further resources and invites contributors to join the Kubernetes Storage Special Interest Group to get involved.
👉 [Read more](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring Batch lead Mahmoud Ben Hassine
In the latest episode of "A Bootiful Podcast," Spring Batch lead Mahmoud Ben Hassine discusses the new developments and features in Spring Batch as it moves into the Spring Boot 4 generation. The conversation highlights the enhancements and innovations in the project, offering insights for Spring fans and developers interested in batch processing.
👉 [Read more](https://spring.io/blog/2025/09/25/a-bootiful-podcast-mahmoud-ben-hassine)

## 🔹 Docker - The Trust Paradox: When Your AI Gets Catfished
The blog post titled "The Trust Paradox: When Your AI Gets Catfished" discusses a new type of security threat called MCP-enabled attacks. These attacks are not technically sophisticated, but rather exploit the trust relationships within a team. Hackers mimic trusted sources, like agencies or collaborators that teams have worked with for years, to deceive AI systems. The post highlights the vulnerability in assuming trust, as design and DevOps teams often rely on files and communications from known partners, making it easier for attackers to infiltrate systems by posing as these trusted entities.
👉 [Read more](https://www.docker.com/blog/mcp-prompt-injection-trust-paradox/)

## 🔹 Java - JEPs in JDK 25 Integrated Since JDK 21
The blog post provides a summary of Java Enhancement Proposals (JEPs) that have been integrated into the Java Development Kit (JDK) from version 22 up to the upcoming JDK 25, following the previous long-term-support release, JDK 21. It excludes any preview and incubator JEPs that have been superseded by later proposals. Each JEP is listed with the specific JDK release version in which it was integrated, offering a clear overview of the new features and improvements that have been added to the JDK since version 21.
👉 [Read more](https://inside.java/2025/09/26/jeps-since-jdk-21/)

## 🔹 Golang - Flight Recorder in Go 1.25
The blog post discusses the introduction of a new tool called "flight recorder" in Go 1.25. This tool is part of the diagnostic toolbox and is designed to help developers monitor and troubleshoot their Go applications more effectively. The flight recorder captures and logs information about the application's behavior, allowing developers to analyze and identify issues. This addition aims to enhance the overall performance and reliability of applications built with Go. For more details, readers are encouraged to visit the provided link to the full blog post.
👉 [Read more](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
The blog post announces the release of the first Alpha version for Helm v4, marking a significant milestone in its development. It provides insights into the current status of Helm v4, outlines upcoming steps, and encourages community involvement in the ongoing development process. The post aims to engage the broader Helm community by sharing details about the project's progress and inviting contributions as it moves closer to the final release.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

