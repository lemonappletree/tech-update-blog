# 🛠️ 2025-05-28 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
The blog post announces that the in-place Pod resize feature, introduced as alpha in Kubernetes v1.27, has now graduated to Beta and will be enabled by default in Kubernetes v1.33. This feature allows changing CPU and memory resources for running containers without needing a restart, making resource management more flexible and less disruptive, particularly for stateful applications and batch jobs. The post details the benefits of in-place Pod resizing, such as reduced disruption, improved resource utilization, and faster scaling. It also lists changes since the alpha release, including the introduction of a `resize` subresource for modifying Pod resources, support for resizing sidecar containers, and various stability and reliability enhancements. Looking ahead, the community plans to continue improving the feature's stability, integrate it with VerticalPodAutoscaler (VPA), and gather user feedback to prioritize future enhancements. Users are encouraged to experiment with the feature and provide feedback through Kubernetes communication channels.
👉 [Read more](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - This Week in Spring (AI) - May 27th, 2025
The blog post "This Week in Spring (AI) - May 27th, 2025" discusses a busy week for the author, who traveled to various cities in Europe for Spring events, including JForum in Stockholm, Spring I/O in Barcelona, and JNation.pt in Coimbra. The post highlights the release of Spring AI 1.0, which supports a variety of AI models and vector stores. Several companies, including Microsoft Azure, AWS, Google, Elastic, Redis, MongoDB, and Oracle, have published content on the new Spring AI release. The blog also mentions other updates in the Spring ecosystem, including new releases of Spring Data, Spring Integration, and Spring Boot, as well as the introduction of Spring Data AOT repositories for improved performance. The post emphasizes the vibrant Spring community and the numerous resources available for developers to explore these updates.
👉 [Read more](https://spring.io/blog/2025/05/27/this-week-in-spring-may-27th-2025)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
The blog post discusses Docker's introduction of Docker Hardened Images, which are designed to be secure, minimal, and ready for production use. Docker has always prioritized enabling developers to build, share, and run software efficiently and securely. With Docker Hub facilitating software delivery on a massive scale, hosting over 14 million images and handling more than 11 billion pulls monthly, Docker has gained valuable insights into modern software development practices. These insights have informed the creation of Docker Hardened Images, which aim to enhance software security and streamline production processes.
👉 [Read more](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - JEP targeted to JDK 25: 510: Key Derivation Function API
The blog post discusses the inclusion of JEP 510, which introduces a Key Derivation Function (KDF) API, as a target for JDK 25. This new API is intended to provide a standardized way for developers to derive cryptographic keys from passwords or other cryptographic material within Java applications, improving security and ease of use. The JEP aims to address the lack of a unified KDF mechanism in Java, making it easier for developers to implement secure key derivation processes. The post likely provides further details on the proposed API and its anticipated benefits for Java developers.
👉 [Read more](https://inside.java/2025/05/26/jep510-target-jdk25/)

## 🔹 Golang - Go Cryptography Security Audit
The blog post discusses a security audit of Go's cryptography libraries conducted by the security firm Trail of Bits. The purpose of the audit was to ensure the robustness and security of the cryptographic implementations in Go. The post likely outlines the findings of the audit, any identified vulnerabilities, and the steps taken to address them, reinforcing Go's commitment to maintaining secure cryptographic practices.
👉 [Read more](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London, UK, from April 1 to 4. With Helm 4 in development, the team invites attendees to engage in discussions with Helm maintainers during talk sessions and visit their booth in the Project Pavilion. The post provides details on various Helm-related activities planned for the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

