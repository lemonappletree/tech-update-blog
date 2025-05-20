# 🛠️ 2025-05-20 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
The blog post announces that the in-place Pod resize feature, initially introduced as an alpha feature in Kubernetes v1.27, has been promoted to Beta and will be enabled by default starting with Kubernetes v1.33. This feature allows users to adjust CPU and memory resources for running Pods without requiring a restart, which is particularly beneficial for stateful applications, long-running batch jobs, and workloads sensitive to restarts. The in-place Pod resize offers reduced disruption, improved resource utilization, and faster scaling. Key changes from alpha to beta include the introduction of a `resize` subresource for modifying Pod resources, new conditions for reporting resize status, and support for resizing sidecar containers. Enhancements have been made to improve stability, reliability, and performance. The Kubernetes community will continue to focus on hardening the feature, addressing current limitations, and integrating with the VerticalPodAutoscaler. Users are encouraged to provide feedback as the feature progresses through Beta.
👉 [Read more](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring Security 6.3.10 Released
The blog post announces the release of Spring Security version 6.3.10. It invites readers to view the changelog for detailed updates and provides links to the project page, GitHub repository, issues tracker, and documentation for further information.
👉 [Read more](https://spring.io/blog/2025/05/19/spring-security-6-3-10)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
The tech blog post introduces Docker Hardened Images, which are designed to be secure, minimal, and production-ready. Docker has consistently aimed to support developers in building, sharing, and running software efficiently and securely. With Docker Hub facilitating software delivery on a global scale—hosting over 14 million images and handling more than 11 billion pulls each month—Docker has gained valuable insights into modern software development practices. This new offering focuses on enhancing security and streamlining the deployment process for developers.
👉 [Read more](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - JEP targeted to JDK 25: 513: Flexible Constructor Bodies
The blog post discusses JEP 513, which is targeted for inclusion in JDK 25. This JEP aims to introduce "Flexible Constructor Bodies" to the Java programming language. The proposal allows for more flexibility in how constructors are defined and implemented, potentially improving code readability and maintainability. The post provides an overview of the JEP's goals and its expected impact on Java development once integrated into JDK 25. For more detailed information, readers are encouraged to visit the provided link.
👉 [Read more](https://inside.java/2025/05/19/jep513-target-jdk25/)

## 🔹 Golang - Go Cryptography Security Audit
The blog post titled "Go Cryptography Security Audit" discusses the security audit conducted on Go's cryptography libraries by the security firm Trail of Bits. The audit aimed to evaluate the security and robustness of these libraries. The detailed findings and recommendations from the audit can be accessed through the provided link to the Go blog.
👉 [Read more](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1 to 4. They are working on Helm 4, which is expected to be released later in the year. Attendees are encouraged to engage with Helm maintainers during talk sessions and visit the Helm booth at the Project Pavilion. The post provides further details about Helm-related activities throughout the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

