# 🛠️ 2025-05-21 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
The blog post announces that the "in-place Pod resize" feature, also known as In-Place Pod Vertical Scaling, has graduated to Beta in Kubernetes v1.33 and is enabled by default. This feature, introduced as alpha in v1.27, allows for changing CPU and memory resources of a running Pod without requiring a restart, benefiting stateful services and workloads sensitive to restarts. Key benefits include reduced disruption, improved resource utilization, and faster scaling. The Beta release includes changes like a new `resize` subresource for modifying Pod resources, enhanced stability, and support for sidecar containers. Future work includes improving stability, addressing limitations, and integrating with VerticalPodAutoscaler (VPA). The community is encouraged to provide feedback as the feature moves through Beta.
👉 [Read more](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring for Apache Pulsar 1.1.12 and 1.2.6 are now available
The blog post announces the release of Spring for Apache Pulsar versions 1.1.12 and 1.2.6, which are now available on Maven Central. These versions will be included in the upcoming Spring Boot releases 3.3.12 and 3.4.6. For more detailed information, readers are encouraged to check the release notes for both versions.
👉 [Read more](https://spring.io/blog/2025/05/21/spring-for-apache-pulsar-1-1-12-and-1-2-6-are-now-available)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
The blog post titled "Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production" highlights Docker's ongoing commitment to helping developers build, share, and run software efficiently and securely. Docker Hub, a key component of this ecosystem, facilitates global software delivery with over 14 million images and more than 11 billion pulls each month. This immense scale provides Docker with valuable insights into modern software development practices. The introduction of Docker Hardened Images aims to enhance security and streamline the production readiness of containerized applications, reinforcing Docker’s role in the software development landscape.
👉 [Read more](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - Towards a JSON API for the JDK
The blog post discusses the development of a JSON API for the Java Development Kit (JDK). It outlines the initial ideas and plans for integrating JSON processing capabilities directly into the JDK, which would provide developers with built-in tools for handling JSON data without relying on external libraries. The post emphasizes the benefits of having a standardized JSON API, such as improved performance and consistency across Java applications. It also invites feedback and collaboration from the Java community to refine the proposal and ensure it meets the needs of developers.
👉 [Read more](https://inside.java/2025/05/20/json-api-jdk/)

## 🔹 Golang - Go Cryptography Security Audit
The tech blog post titled "Go Cryptography Security Audit" discusses a security audit conducted by Trail of Bits on Go's cryptography libraries. The audit aimed to assess and improve the security and reliability of these libraries. The findings and recommendations from the audit help ensure that Go's cryptographic components remain robust and secure. For more detailed information, readers can visit the provided link to the full blog post.
👉 [Read more](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will attend KubeCon + CloudNativeCon EU 2025 in London from April 1-4. They are working on Helm 4, which is expected to be released later in the year. The post invites attendees to engage with the Helm maintainers during talk sessions and at their booth in the Project Pavilion. It also provides details on various Helm-related activities happening throughout the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

