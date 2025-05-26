# 🛠️ 2025-05-26 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
The blog post announces the graduation of the "in-place Pod resize" feature to Beta in Kubernetes v1.33, which allows for changes to CPU and memory resources of a running Pod without requiring a restart. This feature, first introduced as alpha in v1.27, enhances resource management by reducing disruption and improving resource utilization. Key changes from the alpha stage include a new `resize` subresource to modify Pod resources, a revised status reporting system, and support for sidecar containers. Enhancements have been made for stability and reliability, including refined resource management and improved resize detection. The community aims to further stabilize the feature, integrate it with VerticalPodAutoscaler, and gather user feedback for future improvements. Users can start experimenting with this feature in v1.33 and are encouraged to provide feedback via Kubernetes communication channels.
👉 [Read more](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring for Apache Pulsar 1.1.12 and 1.2.6 are now available
The blog post announces the release of Spring for Apache Pulsar versions 1.1.12 and 1.2.6, which are now available on Maven Central. These versions will be part of the upcoming Spring Boot releases 3.3.12 and 3.4.6. The post encourages readers to check the release notes for more detailed information.
👉 [Read more](https://spring.io/blog/2025/05/26/spring-for-apache-pulsar-1-1-12-and-1-2-6-are-now-available)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
The blog post introduces Docker Hardened Images, which are designed to be secure, minimal, and ready for production use. Docker has always aimed to provide an efficient and secure platform for developers to build, share, and run software. Docker Hub, which facilitates global software delivery, hosts over 14 million images and receives more than 11 billion pulls each month. This extensive usage provides Docker with valuable insights into modern software development practices. The new Docker Hardened Images are an extension of Docker's commitment to security and efficiency in software development.
👉 [Read more](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - Pattern Matching in Java: Better Code, Better APIs
The blog post discusses the evolution of Java's `switch` and `instanceof` constructs, which have been integral to data introspection since Java 1.0. These constructs have now advanced to support comprehensive pattern matching, allowing developers to write cleaner and more efficient implementation code. The post also explores the potential impact of pattern matching on the future of API development and core Java features like serialization.
👉 [Read more](https://inside.java/2025/05/24/javaone-pattern-matching/)

## 🔹 Golang - Go Cryptography Security Audit
The blog post titled "Go Cryptography Security Audit" discusses a security audit conducted by Trail of Bits on Go's cryptography libraries. The audit aimed to evaluate the security and robustness of these libraries to ensure they meet high standards. The post likely details the findings and recommendations from the audit, highlighting any vulnerabilities discovered and improvements made to strengthen Go's cryptography infrastructure.
👉 [Read more](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The Helm team is attending KubeCon + CloudNativeCon EU 2025 in London from April 1-4. They will be discussing the upcoming release of Helm 4. Attendees can engage with Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion. The blog post provides more details about Helm-related activities during the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

