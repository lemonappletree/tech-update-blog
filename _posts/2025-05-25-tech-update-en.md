# 🛠️ 2025-05-25 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
The tech blog post announces the graduation of the "in-place Pod resize" feature in Kubernetes to Beta status, starting from version 1.33. This feature, also known as In-Place Pod Vertical Scaling, allows for the adjustment of CPU and memory resources for running Pods without requiring restarts, reducing disruption for stateful applications and enhancing resource utilization. Key updates include the introduction of a "resize" subresource for modifying Pod resources, better status tracking through Pod conditions, and support for resizing sidecar containers. The feature has undergone significant improvements since its alpha version, enhancing stability, reliability, and efficiency. Future development will focus on stability, addressing limitations, integrating with VerticalPodAutoscaler, and gathering user feedback. The feature is enabled by default in Kubernetes v1.33, and users are encouraged to experiment with it and provide feedback.
👉 [Read more](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring for Apache Pulsar 1.1.12 and 1.2.6 are now available
The blog post announces the release of Spring for Apache Pulsar versions 1.1.12 and 1.2.6, which are now available on Maven Central. These versions will be included in the upcoming releases of Spring Boot versions 3.3.12 and 3.4.6, respectively. For more detailed information, readers are directed to the release notes for versions 1.1.12 and 1.2.6.
👉 [Read more](https://spring.io/blog/2025/05/25/spring-for-apache-pulsar-1-1-12-and-1-2-6-are-now-available)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
The blog post introduces Docker Hardened Images, which are designed to be secure, minimal, and ready for production use. Docker has always aimed to help developers build, share, and run software efficiently and securely. Docker Hub, with its vast repository of over 14 million images and over 11 billion pulls each month, plays a crucial role in global software delivery. This extensive scale provides Docker with unique insights into modern software development practices. The new hardened images are part of Docker's ongoing efforts to enhance security and reliability for developers worldwide.
👉 [Read more](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - Pattern Matching in Java: Better Code, Better APIs
The blog post titled "Pattern Matching in Java: Better Code, Better APIs" discusses the evolution of the switch and instanceof constructs in Java. Initially introduced in Java 1.0, these constructs have now developed to support full pattern matching, allowing developers to write cleaner and more efficient code. The post explores the current use of switch and instanceof and considers how pattern matching could influence future API development and core Java features like serialization.
👉 [Read more](https://inside.java/2025/05/24/javaone-pattern-matching/)

## 🔹 Golang - Go Cryptography Security Audit
The blog post discusses a security audit conducted by Trail of Bits on Go's cryptography libraries. It highlights the importance of ensuring the security and reliability of these libraries, which are crucial for the safe development of applications using the Go programming language. The audit aimed to identify any potential vulnerabilities or weaknesses and provide recommendations for improvements. The findings and subsequent enhancements are detailed in the full report linked in the blog.
👉 [Read more](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1st to 4th. They are working on Helm 4, expected to be released later in the year. Attendees can engage with the Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion. The post provides details on various Helm-related activities taking place during the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

