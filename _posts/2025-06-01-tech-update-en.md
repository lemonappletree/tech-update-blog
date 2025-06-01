# 🛠️ 2025-06-01 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
The blog post announces the graduation of the "in-place Pod resize" feature to Beta status in Kubernetes v1.33, where it will be enabled by default. This feature allows the adjustment of CPU and memory resources in running Pods without needing a restart, which is beneficial for stateful applications and workloads sensitive to restarts. The update includes several enhancements since its alpha release, such as a new `resize` subresource for modifications, improved resource management, sidecar support, and better integration with the Container Runtime Interface (CRI). Looking ahead, the Kubernetes community plans to focus on further stabilizing the feature, integrating it with the VerticalPodAutoscaler (VPA), and gathering user feedback. Users can start experimenting with this feature and provide feedback through standard Kubernetes communication channels.
👉 [Read more](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring Cloud 2025.0.0 (aka Northfields) has been released
The blog post announces the general availability of the Spring Cloud 2025.0.0 release, also known as the Northfields release. It is available on Maven Central, and the release notes can be found on GitHub. The release is compatible with Spring Boot 3.5.0 and includes several notable changes:

1. **Spring Cloud Gateway**: 
   - Adds support for spring-cloud-function and spring-cloud-stream handlers.
   - Introduces a Bucket4jRateLimiter for server webflux.
   - Deprecates WebClientRouting infrastructure, to be removed in version 5.0.
   - New module and starter names are introduced, with deprecated names providing log warnings.
   - Migration to new property prefixes aligning with new module names.

2. **Spring Cloud Config**: 
   - Supports YAML specific profile documents in AWS S3 buckets.

3. **Spring Cloud Kubernetes**: 
   - Treats Kubernetes as a composite config source.
   - Upgrades to Fabric8 7.3.1, introducing a breaking change.

4. **Spring Cloud Circuitbreaker**: 
   - Adds support for reactive bulkheads.

5. **Spring Cloud Netflix**: 
   - Allows customization of Apache HTTP Client 5 RequestConfig in EurekaClientHttpRequestFactorySupplier.

Additionally, the blog lists updated modules and their versions, providing links to issues and release notes. Feedback is welcomed through GitHub, Gitter, Stack Overflow, or X. The post also provides instructions for getting started with Maven and Gradle.
👉 [Read more](https://spring.io/blog/2025/05/29/spring-cloud-2025-0-0-is-abvailable)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
The blog post introduces Docker Hardened Images, which are designed to be secure, minimal, and ready for production use. Docker has always aimed to help developers efficiently and securely build, share, and run software. With Docker Hub supporting global software delivery, hosting over 14 million images and handling more than 11 billion pulls monthly, Docker has gained valuable insights into modern software development practices. The new Hardened Images leverage this experience to provide robust, production-ready solutions for developers.
👉 [Read more](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - The Inside Java Newsletter: Java’s 30th Birthday &amp; JavaOne!
The Inside Java Newsletter for May 2025 celebrates Java's 30th birthday and begins sharing content from JavaOne 2025. This issue includes podcast interviews, community news, and the latest technical videos to help developers keep up with Java innovations. Future issues will feature details about a new website for Java learning aimed at students and teachers. Produced by the Java Developer Relations team, the newsletter highlights technical content from the Java Platform Group. Readers are encouraged to check the archives, subscribe, and share with friends.
👉 [Read more](https://inside.java/2025/05/28/inside-java-newsletter/)

## 🔹 Golang - Go Cryptography Security Audit
The blog post titled "Go Cryptography Security Audit" discusses the recent security audit performed on Go's cryptography libraries by Trail of Bits. The audit aimed to evaluate the security and robustness of these libraries, ensuring they meet high standards for cryptographic implementations. The post likely details the findings of the audit, any recommended improvements, and the steps Go's development team plans to take to address any identified issues. For more detailed information, readers are encouraged to visit the provided link to the full blog post.
👉 [Read more](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1 to 4. Attendees can engage with Helm maintainers during talk sessions and at the Helm booth in the Project Pavilion. The post also mentions that Helm 4 is in development and encourages participants to join discussions about it. More details on Helm-related activities throughout the event are provided in the post.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

