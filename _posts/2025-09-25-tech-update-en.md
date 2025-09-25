# 🛠️ 2025-09-25 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.34: Pod Level Resources Graduated to Beta
The blog post announces the graduation of the Pod Level Resources feature to Beta in Kubernetes v1.34, where it is now enabled by default. This feature offers a new level of flexibility by allowing CPU and memory resources to be specified at the Pod level, rather than just at the container level. This approach simplifies resource management by reducing the need for per-container resource specifications, especially in multi-container Pods. It also allows for more efficient resource sharing within Pods, preventing performance bottlenecks from sidecar containers. Pod-level resource requests and limits take precedence over container-level specifications, providing a consolidated method for enforcing resource boundaries and influencing Quality of Service (QoS) classes. The feature is designed to integrate smoothly with existing Kubernetes functionalities, though it does not support in-place resizing for running Pods or apply to Windows Pods. Users are encouraged to provide feedback as the feature progresses through its Beta phase.
👉 [Read more](https://kubernetes.io/blog/2025/09/22/kubernetes-v1-34-pod-level-resources/)

## 🔹 Spring Boot - This Week in Spring - September 23rd, 2025
The blog post "This Week in Spring - September 23rd, 2025" shares exciting updates and events in the Spring community. The author is preparing for several conferences, including "Commit Your Code" in Texas and "Devoxx Belgium." Highlights from the community include new features in Spring Framework 7, updates in Spring AI 1.0.2, and the release of Spring Modulith 2.0 M3. The post also covers new versions of Spring Boot, Spring Batch, Spring Integration, and Spring for Apache Kafka. It features a podcast with Spencer Gibb, a discussion with Spring cofounders Rod Johnson and Juergen Hoeller, and insights into running a Spring Boot application on JRuby by Charles Nutter. Additionally, it mentions articles on streaming multipart data, implementing a simple rules engine, and optimizing integration tests with Spring. The post encourages readers to explore these updates and resources.
👉 [Read more](https://spring.io/blog/2025/09/23/this-week-in-spring-september-23rd-2025)

## 🔹 Docker - MCP Horror Stories: The Drive-By Localhost Breach
The blog post titled "MCP Horror Stories: The Drive-By Localhost Breach" is part of a series exploring security incidents related to AI infrastructure vulnerabilities. It focuses on a specific breach involving the Model Context Protocol (MCP), which is pivotal for integrating AI agents with development environments. The post highlights how this breach exposed significant security flaws, emphasizing the need for robust protection mechanisms. It also showcases how Docker's MCP Gateway can offer enterprise-grade security against complex attack vectors, reinforcing the importance of securing AI integrations.
👉 [Read more](https://www.docker.com/blog/mpc-horror-stories-cve-2025-49596-local-host-breach/)

## 🔹 Java - JDK 25 Security Enhancements
The blog post discusses the security enhancements introduced in JDK 25, which was released on September 16, 2025. The author has compiled a list of the most interesting and useful security updates in this release and categorized them into areas such as cryptography and TLS. This organization helps readers easily identify changes relevant to each specific area of security.
👉 [Read more](https://inside.java/2025/09/24/jdk25-security-enhancements/)

## 🔹 Golang - It's survey time! How has Go has been working out for you?
The blog post announces a survey aimed at gathering feedback from Go programming language users. The goal is to understand how Go has been working for its community and to gather insights that could influence the future development of the language. The survey is an opportunity for users to share their experiences, challenges, and suggestions, ultimately helping to shape the evolution of Go.
👉 [Read more](https://go.dev/blog/survey2025-announce)

## 🔹 Helm - Path To Releasing Helm v4
The blog post announces the release of the first Alpha version of Helm v4, marking a significant milestone in its development. It provides details on the current progress of Helm v4 and outlines opportunities for the broader community to participate and contribute to the project as it approaches its final stages. The post emphasizes community involvement and collaboration in the ongoing development process.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

