# 🛠️ 2025-06-03 Tech Update Summary

## 🔹 Kubernetes - Start Sidecar First: How To Avoid Snags
The blog post discusses strategies to ensure that sidecar containers in Kubernetes start before the main application, a process that is more complex than it might appear. With the Kubernetes v1.29.0 release, sidecar containers can be defined in the `.spec.initContainers` field with `restartPolicy: Always`, ensuring they start before the main app and terminate after it. However, this often results in almost parallel starts, which might not be desirable if the main application depends on the sidecar being fully operational. The post explores various methods to manage this sequence, including readiness probes, startup probes, and postStart lifecycle hooks. A readiness probe doesn't ensure the main app waits for the sidecar to be ready, while a startup probe can delay the main app's start until the sidecar is ready. The postStart hook can also be used but requires custom logic. The article includes YAML code examples to illustrate these configurations, aiming to help readers deploy applications more gracefully with a sidecar dependency.
👉 [Read more](https://kubernetes.io/blog/2025/06/03/start-sidecar-first/)

## 🔹 Spring Boot - Spring Cloud 2022.0.11 (aka Kilburn) Has Been Released
The Spring Cloud team has announced the release of Spring Cloud 2022.0.11, also known as Kilburn. This release is available for support customers and can be accessed through Broadcom's package distribution. Key updates in this release include compatibility with Spring Boot versions 3.0.20 and 3.1.17, as well as dependency upgrades across various components such as Spring Cloud Commons, Task, Config, Netflix, OpenFeign, Gateway, Contract, Kubernetes, and Vault. Additionally, the release addresses security vulnerabilities with fixes for CVE-2025-22232 in Spring Cloud Config and CVE-2025-41235 in Spring Cloud Gateway.
👉 [Read more](https://spring.io/blog/2025/06/02/spring-cloud-2022-0-11-aka-kilburn-has-been-released)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
The blog post introduces Docker Hardened Images, which are designed to be secure, minimal, and ready for production use. Docker has always prioritized enabling developers to efficiently and securely build, share, and run software. With Docker Hub hosting over 14 million images and facilitating more than 11 billion pulls each month, Docker has gained valuable insights into modern software development practices. The new Hardened Images offer enhanced security, making them ideal for production environments.
👉 [Read more](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - JEP targeted to JDK 25: 506: Scoped Values
The blog post discusses JEP 506, which is aimed at being included in JDK 25. This JEP introduces "Scoped Values," a feature designed to enhance Java's ability to handle values with a specific scope. This addition is expected to improve the language's efficiency and flexibility in managing scoped data. The post likely provides insights into the benefits, potential use cases, and implementation details of this new feature, contributing to the ongoing evolution of the Java programming language.
👉 [Read more](https://inside.java/2025/06/02/jep506-target-jdk25/)

## 🔹 Golang - Go Cryptography Security Audit
The blog post titled "Go Cryptography Security Audit" discusses the recent security audit conducted by Trail of Bits on Go's cryptography libraries. The audit aimed to evaluate the security of these libraries and ensure their robustness and reliability. The blog provides insights into the audit process and its findings, highlighting the steps taken to address any identified issues and improve the overall security of Go's cryptographic components.
👉 [Read more](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London, UK, from April 1 to 4. The team will discuss the upcoming release of Helm 4 and engage with participants at talk sessions and the Helm booth in the Project Pavilion. The post encourages attendees to join these activities to learn more about Helm and its future developments.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

