# 🛠️ 2025-09-24 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.34: Pod Level Resources Graduated to Beta
The blog post announces that the Pod Level Resources feature in Kubernetes has reached Beta status with the release of Kubernetes v1.34 and is enabled by default. This feature allows for specifying CPU and memory resources at the Pod level, providing a new layer of flexibility in resource management. It simplifies resource allocation by reducing the need for granular per-container specifications, promoting efficient resource sharing within Pods, and preventing performance bottlenecks caused by sidecar containers. Pod-level requests and limits take precedence over container-level specifications, ensuring a robust way to enforce resource boundaries. Additionally, this feature affects Quality of Service (QoS) class determination and Out-Of-Memory (OOM) score adjustments. The post includes examples of how to specify resources for Pods and discusses the feature's limitations, such as the lack of support for in-place resizing and Windows Pods. It encourages users to provide feedback as the feature progresses through its Beta phase.
👉 [Read more](https://kubernetes.io/blog/2025/09/22/kubernetes-v1-34-pod-level-resources/)

## 🔹 Spring Boot - This Week in Spring - September 23rd, 2025
The blog post "This Week in Spring - September 23rd, 2025" highlights various events and updates in the Spring ecosystem. The author is preparing for several conferences, including Commit Your Code, Dev2Next, Devoxx Belgium, and CloudFoundry Days. Key updates include the introduction of new HTTP Service Clients in Spring Framework 7, enhancements in Spring AI 1.0.2, the release of Spring Modulith 2.0 M3, and several Spring Boot versions now available. The post also mentions a podcast with Spring Cloud lead Spencer Gibb, new releases such as Spring Batch 6.0.0 M3 and Spring Integration 7.0 M3, and a preview of running a Spring Boot application on JRuby. Additional resources include articles on optimizing integration tests and implementing a simple rules engine using Spring. The blog also notes a reunion of Spring cofounders at Spring I/O 2025 and a Spring news roundup from InfoQ.
👉 [Read more](https://spring.io/blog/2025/09/23/this-week-in-spring-september-23rd-2025)

## 🔹 Docker - MCP Horror Stories: The Drive-By Localhost Breach
The blog post, titled "MCP Horror Stories: The Drive-By Localhost Breach," is the fourth installment in a series exploring real-world security incidents that reveal significant vulnerabilities in AI infrastructure. It highlights the importance of robust security measures, particularly in the context of the Model Context Protocol (MCP), which has revolutionized the integration of AI agents into development environments. The post discusses how Docker's MCP Gateway offers enterprise-level protection against advanced attack methods, emphasizing the need for heightened security to protect against potential breaches.
👉 [Read more](https://www.docker.com/blog/mpc-horror-stories-cve-2025-49596-local-host-breach/)

## 🔹 Java - JavaFX 25 Highlights
The blog post introduces JavaFX 25, highlighting its new features and improvements. JavaFX 25 is specifically designed to be compatible with JDK 25 but also works with JDK 23 and later versions. The post likely details enhancements that improve user interface development, performance, and integration with the latest Java developments.
👉 [Read more](https://inside.java/2025/09/23/javafx-25/)

## 🔹 Golang - It's survey time! How has Go has been working out for you?
The blog post announces a survey for Go users to provide feedback on their experiences with the programming language. The purpose of the survey is to gather insights and opinions from the community to help guide the future development and improvement of Go. Participants are encouraged to share their thoughts to help shape the direction of the language and its ecosystem.
👉 [Read more](https://go.dev/blog/survey2025-announce)

## 🔹 Helm - Path To Releasing Helm v4
The blog post discusses the release of the first Alpha version of Helm v4, marking a significant milestone in its development. It outlines the current progress, upcoming steps, and invites the broader community to participate in the process. The post provides insights into the new features and improvements expected in Helm v4 and encourages feedback and contributions from users and developers as the project nears completion.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

