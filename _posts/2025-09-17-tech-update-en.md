# 🛠️ 2025-09-17 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.34: Moving Volume Group Snapshots to v1beta2
The blog post discusses the update of Kubernetes to version 1.34, which includes moving the Volume Group Snapshots feature to version v1beta2. Initially introduced as an Alpha feature in Kubernetes 1.27 and moved to Beta in 1.32, Volume Group Snapshots allow users to take crash-consistent snapshots of a set of volumes using extension APIs for group snapshots. This feature is only supported for CSI volume drivers. A new issue was identified during testing, leading to changes in the API and the release of a new beta version. The v1beta2 introduces a new VolumeSnapshotInfo struct and VolumeSnapshotInfoList to better handle snapshot information. Existing API objects will be converted to the new format using a conversion webhook. The post also mentions plans to move this feature to general availability (GA) in the future, depending on feedback and adoption. It provides links to further resources and acknowledges the contributors involved in the development. The blog encourages interested individuals to join the Kubernetes Storage Special Interest Group (SIG) or the Data Protection Working Group to get involved in the project's development.
👉 [Read more](https://kubernetes.io/blog/2025/09/16/kubernetes-v1-34-volume-group-snapshot-beta-2/)

## 🔹 Spring Boot - This Week in Spring - September 16th, 2025
This week's edition of "This Week in Spring" celebrates the release of Java 25 and GraalVM 25, highlighting several new features. Notable updates include module import declarations for easier package imports and support for Java scripts, allowing concise coding without a public class or static main method. Additionally, the new AOT support for method profiling enhances startup efficiency. The post also provides a roundup of recent Spring releases, including updates for Spring for GraphQL, Spring Security, Spring AMQP, Spring Data, and more. It mentions various new features, security fixes, and a podcast with Purnima Padmanabhan. The post encourages trying out the new Java version using SDKMAN.io and hints at upcoming Spring Initializr support for Java 25.
👉 [Read more](https://spring.io/blog/2025/09/16/this-week-in-spring-september-16th-2025)

## 🔹 Docker - MCP Security: A Developer’s Guide
The blog post titled "MCP Security: A Developer’s Guide" discusses the Model Context Protocol (MCP), which was released by Anthropic in November 2024. MCP has rapidly gained popularity as a crucial framework that connects AI agents with various tools, APIs, and data sources. The protocol allows developers to configure AI agents with minimal effort, enabling them to perform tasks such as searching code, opening tickets, querying SaaS systems, and deploying applications. The blog provides insights into how MCP functions as a secure and efficient bridge in the AI ecosystem.
👉 [Read more](https://www.docker.com/blog/mcp-security-explained/)

## 🔹 Java - The Arrival of Java 25
The blog post announces the release of JDK 25, emphasizing its availability for developers, enterprises, and end-users. Oracle highlights the enhancements and new features included in this version, which aim to improve performance, security, and developer productivity. The release continues Java's tradition of providing a robust and versatile platform for building applications. Readers are encouraged to explore the new capabilities of Java 25 through the provided link.
👉 [Read more](https://inside.java/2025/09/16/the-arrival-of-java-25/)

## 🔹 Golang - It's survey time! How has Go has been working out for you?
The blog post announces a survey for Go programming language users, inviting them to share their experiences and feedback. The aim is to gather insights that will help shape the future development of Go. Participants' input will be crucial in identifying areas for improvement and innovation, ensuring that the language continues to meet the needs of its community.
👉 [Read more](https://go.dev/blog/survey2025-announce)

## 🔹 Helm - Path To Releasing Helm v4
The blog post announces the release of the first Alpha version of Helm v4, marking a significant milestone in its development. With Helm v4 nearing completion, the post provides insights into the development process and encourages the broader community to participate and contribute. It outlines the current status, upcoming steps, and ways for community members to get involved in shaping the final version. The post serves as an invitation for feedback and collaboration from users and developers alike.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

