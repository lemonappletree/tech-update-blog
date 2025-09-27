# 🛠️ 2025-09-27 Tech Update Summary

## 🔹 Kubernetes - Announcing Changed Block Tracking API support (alpha)
The blog post announces the alpha support for a Changed Block Tracking API in Kubernetes, which aids CSI storage drivers in identifying changed blocks in PersistentVolume snapshots. This feature allows for more efficient backup operations by focusing on modified data instead of scanning entire volumes, thus reducing resource usage and backup time. Initially, it supports only block volumes, not file volumes. The post details the benefits of the API, key components, and implementation requirements for storage providers and backup solutions. It also provides guidance on getting started with the feature and encourages community involvement in further development. The post highlights the potential for the feature to move to beta in future releases based on feedback and adoption.
👉 [Read more](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring Batch lead Mahmoud Ben Hassine
The blog post is about a podcast episode where the host talks with Mahmoud Ben Hassine, the lead of the Spring Batch project. They discuss the newest developments and features in Spring Batch as part of the Spring Boot 4 generation.
👉 [Read more](https://spring.io/blog/2025/09/25/a-bootiful-podcast-mahmoud-ben-hassine)

## 🔹 Docker - The Trust Paradox: When Your AI Gets Catfished
The blog post titled "The Trust Paradox: When Your AI Gets Catfished" discusses a new type of cyber attack that targets AI systems by exploiting trust-based relationships. These MCP-enabled attacks aren't about technical complexity; rather, hackers use deceptive tactics similar to catfishing to manipulate AI. The attacks are effective because they take advantage of the inherent trust between development teams and their long-standing partners, like designers expecting files from familiar agencies or DevOps teams relying on trusted sources. The post highlights the vulnerability of AI systems when trust is misused, emphasizing the need for vigilance against such deceptive practices.
👉 [Read more](https://www.docker.com/blog/mcp-prompt-injection-trust-paradox/)

## 🔹 Java - JEPs in JDK 25 Integrated Since JDK 21
The blog post provides a summary of all the Java Enhancement Proposals (JEPs) that have been integrated into the JDK from version 22 to version 25, following the previous long-term-support release, JDK 21. It specifically excludes any preview and incubator JEPs that were later replaced by subsequent JEPs in these versions. The post lists the JEPs along with the specific JDK release in which each was integrated, offering a comprehensive overview of the new features and improvements introduced in the latest JDK versions.
👉 [Read more](https://inside.java/2025/09/26/jeps-since-jdk-21/)

## 🔹 Golang - Flight Recorder in Go 1.25
The blog post discusses the introduction of a new feature called "Flight Recorder" in Go 1.25. This tool is part of the diagnostic toolbox and is designed to aid developers in capturing and analyzing program execution. The Flight Recorder provides detailed insights into the runtime behavior of Go applications, helping developers identify and troubleshoot issues more effectively. The post likely elaborates on how to use this tool and its benefits for enhancing performance and debugging capabilities in Go applications.
👉 [Read more](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
The blog post discusses the release of the first Alpha version of Helm v4, marking a significant milestone in its development. As Helm v4 approaches its final stages, the post outlines the current progress and encourages community involvement. It provides insights into the new features and changes expected in this version and invites feedback and contributions from users and developers to help refine and improve the final release.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

