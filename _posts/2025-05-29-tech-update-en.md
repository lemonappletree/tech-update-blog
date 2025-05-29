# 🛠️ 2025-05-29 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
The blog post announces the graduation of the "in-place Pod resize" feature to Beta in Kubernetes v1.33, enabling it by default. This feature allows users to adjust CPU and memory resources for running Pods without needing to restart them, which is beneficial for stateful applications and workloads sensitive to restarts. Key benefits include reduced disruption, improved resource utilization, and faster scaling. Since its alpha release in v1.27, significant improvements have been made, including a new `resize` subresource for modifying resources, better status reporting, sidecar support, and enhanced stability. The community will continue to focus on stability, addressing limitations, integrating with VerticalPodAutoscaler, and gathering user feedback. Users are encouraged to experiment with the feature and provide feedback through Kubernetes communication channels.
👉 [Read more](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring Modulith 1.4 GA, 1.3.6, and 1.2.13 released
The blog post announces the release of Spring Modulith 1.4, alongside versions 1.3.6 and 1.2.13, after half a year of development. The 1.4 release introduces various new features and improvements across several areas, including core module refinements, testing enhancements, event handling performance improvements, and updates to runtime and observability support. Notable changes include the introduction of an SPI for detecting NamedInterfaces, performance fixes for JavaPackage, improved integration test capabilities, and revamped event publication infrastructure. The release also transitions to the Micrometer Observations API for better metrics capturing and introduces a new ModulithEventMetrics API. Additionally, documentation generation and configuration settings have been updated. The release aligns with the latest Spring Boot 3.5 and Framework 6.2, and ArchUnit 1.4. Future plans include preparations for a 2.0 major release in November, with upcoming support in IntelliJ IDEA. For more details, readers are encouraged to check the full changelog linked in the post.
👉 [Read more](https://spring.io/blog/2025/05/28/spring-modulith-1-4-1-3-6-and-1-2-13-released)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
The blog post titled "Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production" highlights Docker's commitment to providing developers with efficient and secure tools for building, sharing, and running software. It introduces Docker Hardened Images, which are designed to be secure, minimal, and production-ready. These images are developed to enhance security and streamline software delivery, leveraging Docker Hub's extensive reach, which includes over 14 million images and more than 11 billion pulls each month. This initiative reflects Docker's unique insight into modern software development and its ongoing efforts to support developers globally.
👉 [Read more](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - The Inside Java Newsletter: Java’s 30th Birthday &amp; JavaOne!
The May 2025 edition of The Inside Java Newsletter marks Java's 30th anniversary and begins sharing content from JavaOne 2025. This issue features podcast interviews, community news, and the latest technical videos to help developers keep up with Java's innovations. Additionally, it teases a new website aimed at teaching Java to students and teachers, with more details to come in future issues. Produced by the Java Developer Relations team, the newsletter highlights content from the Java Platform Group. Readers are encouraged to explore the archives, subscribe, and share the newsletter with others.
👉 [Read more](https://inside.java/2025/05/28/inside-java-newsletter/)

## 🔹 Golang - Go Cryptography Security Audit
The blog post discusses the security audit of Go's cryptography libraries conducted by Trail of Bits. This audit aimed to assess the security and robustness of these libraries, ensuring they meet high standards for cryptographic safety. The audit results and any recommendations for improvements are detailed in the post. For more information, readers can visit the provided link.
👉 [Read more](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will attend KubeCon + CloudNativeCon EU '25 in London, UK, from April 1 to April 4. They will be discussing the upcoming release of Helm 4, which is expected later in the year. Attendees can engage with Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion for more information. The post provides further details on various Helm-related activities scheduled for the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

