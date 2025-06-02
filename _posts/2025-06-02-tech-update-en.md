# 🛠️ 2025-06-02 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
The blog post announces that the "in-place Pod resize" feature, introduced as an alpha feature in Kubernetes v1.27, has graduated to Beta and is enabled by default in Kubernetes v1.33. This feature allows CPU and memory resources for running Pods to be adjusted without requiring a restart, which is beneficial for stateful applications and workloads sensitive to disruptions. Key changes from alpha to beta include the introduction of a "resize" subresource, improved resource management, and sidecar support. The feature enhances resource utilization, reduces disruption, and accelerates scaling. Moving forward, the community plans to enhance the feature's stability, address limitations, integrate it with the VerticalPodAutoscaler (VPA), and gather user feedback. Users are encouraged to experiment with the feature and provide feedback through Kubernetes communication channels.
👉 [Read more](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring Cloud 2025.0.0 (aka Northfields) has been released
The blog post announces the general availability of the Spring Cloud 2025.0.0 (Northfields) release train. It highlights key changes and updates across various Spring Cloud components, including Spring Cloud Gateway, Config, Kubernetes, Circuitbreaker, and Netflix. Notably, Spring Cloud Gateway introduces support for new handlers, a new rate limiter, and deprecates several artifacts and property prefixes. Spring Cloud Config supports YAML profile documents in AWS S3, while Spring Cloud Kubernetes sees a breaking change with an upgrade to Fabric8 7.3.1. The release is compatible with Spring Boot 3.5.0, and all updates can be found on Maven Central. Feedback is encouraged via GitHub, Gitter, Stack Overflow, or X. The post also includes instructions for integrating the release with Maven and Gradle.
👉 [Read more](https://spring.io/blog/2025/05/29/spring-cloud-2025-0-0-is-abvailable)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
The blog post introduces Docker Hardened Images, which are designed to provide secure, minimal, and production-ready container images. Docker has always aimed to help developers build, share, and run software efficiently and securely, and Docker Hub plays a crucial role in this by supporting global software delivery with millions of images and billions of pulls each month. This extensive usage provides Docker with valuable insights into modern software development practices. The new Docker Hardened Images are part of Docker's continued efforts to enhance security and reliability in software development.
👉 [Read more](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - The Inside Java Newsletter: Java’s 30th Birthday &amp; JavaOne!
The Inside Java Newsletter for May 2025 celebrates Java's 30th birthday and shares content from JavaOne 2025. This issue features podcast interviews, community news, and the latest technical videos to help developers keep up with Java innovations. It also announces a new website for learning Java aimed at students and teachers, with more details to come in future issues. Produced by the Java Developer Relations team, the newsletter highlights technical content from the Java Platform Group and encourages readers to explore archives, subscribe, and share with friends.
👉 [Read more](https://inside.java/2025/05/28/inside-java-newsletter/)

## 🔹 Golang - Go Cryptography Security Audit
The blog post discusses the results of a security audit conducted by Trail of Bits on Go's cryptography libraries. The audit aimed to assess the security and reliability of these libraries to ensure they meet high standards. The findings and recommendations from the audit are intended to enhance the security of the Go programming language's cryptographic components. The post likely details specific vulnerabilities found, improvements made, and future plans to maintain robust security in Go's cryptography offerings.
👉 [Read more](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London, UK, from April 1-4. They are working on Helm 4, which is set to be released later in the year. Attendees are encouraged to join discussions with Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion. The post provides more details on Helm-related activities throughout the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

