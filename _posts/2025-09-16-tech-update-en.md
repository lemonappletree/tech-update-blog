# 🛠️ 2025-09-16 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.34: Decoupled Taint Manager Is Now Stable
The blog post discusses the stabilization of the decoupled taint manager in Kubernetes v1.34. This update separates the responsibilities of managing node lifecycle and pod eviction into two different components. Previously, the node lifecycle controller was responsible for both marking nodes as unhealthy with NoExecute taints and evicting pods. Now, a dedicated taint eviction controller handles evictions, while the node lifecycle controller focuses on applying taints. This separation improves code organization and allows for easier enhancements or custom implementations of the taint-based eviction process. The feature gate `SeparateTaintEvictionController` has reached general availability, and users have the option to disable taint-based eviction. More information can be found in the KEP and previous announcements. The post also acknowledges contributors who helped develop this feature.
👉 [Read more](https://kubernetes.io/blog/2025/09/15/kubernetes-v1-34-decoupled-taint-manager-is-now-stable/)

## 🔹 Spring Boot - Spring Security 6.4.10 and 6.5.4 Released
The blog post announces the release of Spring Security versions 6.4.10 and 6.5.4, acknowledging contributions from the team. Both versions include four fixes and several dependency upgrades. Version 6.4.10 will be released alongside Spring Boot 3.4.10, and version 6.5.4 will accompany Spring Boot 3.5.6. These releases also address security vulnerabilities CVE-2025-41248 and CVE-2025-41249. Additional details can be found in the linked Spring Security and Spring Framework release notes. The post provides links to the project page, GitHub repository, issue tracker, and documentation.
👉 [Read more](https://spring.io/blog/2025/09/15/spring-security-6-4-10-and-6-5-4-released)

## 🔹 Docker - The Nine Rules of AI PoC Success: How to Build Demos That Actually Ship
The blog post challenges the claim that "95% of AI Proof of Concepts (PoCs) fail," labeling it as clickbait and unsubstantiated. The author argues that the real issue is not the failure rate itself but the lack of proper tracking and understanding of why PoCs don't transition to full deployment. Drawing from years of experience observing AI development teams, the post aims to provide practical advice. It outlines nine key rules for creating AI demos that successfully move beyond the PoC stage to actual implementation, emphasizing the importance of strategic planning, clear objectives, and effective execution.
👉 [Read more](https://www.docker.com/blog/ai-poc-success-rules/)

## 🔹 Java - All API Additions From Java 21 to 25 #RoadTo25
The blog post titled "All API Additions From Java 21 to 25 #RoadTo25" discusses the new API features introduced in Java versions 21 through 25. It covers several key enhancements, including scoped values, which provide a way to manage values with limited scopes; stream gatherers, which are improvements to the Stream API for better data processing; updates to the class-file API, which facilitate working with Java class files; and the foreign function and memory API, which enhances interaction with non-Java code and memory management. Additionally, the post highlights new additions to Javadoc, improving documentation generation and usability.
👉 [Read more](https://inside.java/2025/09/09/roadto25-api/)

## 🔹 Golang - A new experimental Go API for JSON
The blog post discusses the introduction of experimental support for new JSON handling packages in Go 1.25: `encoding/json/jsontext` and `encoding/json/v2`. These packages aim to improve Go's JSON processing capabilities by providing more efficient and flexible ways to encode and decode JSON data. The blog highlights the motivation behind these updates, the improvements over the existing JSON package, and encourages developers to try out these experimental packages and provide feedback.
👉 [Read more](https://go.dev/blog/jsonv2-exp)

## 🔹 Helm - Path To Releasing Helm v4
The blog post discusses the release of the first Alpha version of Helm v4, marking a significant milestone in its development. As Helm v4 progresses towards its final release, the post outlines the current state of development and encourages the broader community to participate. It provides details on how community members can get involved and contribute to the project, ensuring a collaborative effort in refining and finalizing Helm v4.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

