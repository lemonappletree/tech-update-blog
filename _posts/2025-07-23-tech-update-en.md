# 🛠️ 2025-07-23 Tech Update Summary

## 🔹 Kubernetes - Post-Quantum Cryptography in Kubernetes
The blog post discusses the impact of quantum computing on cryptography, particularly focusing on the Kubernetes ecosystem. It highlights the need for Post-Quantum Cryptography (PQC) to secure cryptographic algorithms against potential attacks from quantum computers. The post explains how quantum computers could break current cryptographic standards like RSA and ECC, emphasizing the urgency of transitioning to PQC algorithms.

In the context of Kubernetes, the article notes that with the release of Kubernetes v1.33 and its use of Go 1.24, the platform now supports hybrid post-quantum key exchange mechanisms by default. This includes the X25519MLKEM768 scheme, enhancing TLS connections' security against future quantum threats. The blog also outlines challenges, such as Go version mismatches and packet size limitations that could affect PQC adoption.

Furthermore, while PQC for key exchange is progressing, the adoption of PQC for digital signatures faces hurdles like larger key sizes and slower performance. The post concludes by urging Kubernetes maintainers to stay informed about these developments to ensure the platform's long-term security.
👉 [Read more](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)

## 🔹 Spring Boot - Spring Authorization Server 2.0.0-M1 available now
The blog post announces the release of the Spring Authorization Server 2.0.0-M1 milestone. It invites users to check the release notes for detailed information and provides resources for getting started, including the reference documentation and samples for setup and configuration. Links to the project page and GitHub issues are also provided for further exploration and feedback.
👉 [Read more](https://spring.io/blog/2025/07/22/spring-authorization-server-2-0-0-M1-available-now)

## 🔹 Docker - Compose Editing Evolved: Schema-Driven and Context-Aware
The blog post discusses enhancements to the Docker Compose editing experience, focusing on schema-driven and context-aware features. Docker is continuously improving Docker Compose by introducing new capabilities, such as provider services, which allow developers to integrate AI models into their multi-container applications using Docker Model Runner. The post emphasizes Docker's commitment to delivering a superior editing experience for Compose files used by developers worldwide.
👉 [Read more](https://www.docker.com/blog/compose-editing-evolved-schema-driven-and-context-aware/)

## 🔹 Java - A Sneak Peek at the Stable Values API
The blog post introduces the Stable Values API, which addresses the limitations of the `@Stable` annotation in Java. Previously, this annotation, used internally in JDK classes, marked fields that change at most once, enhancing performance, energy efficiency, and flexibility. However, it was not accessible to Java applications, limiting its use. The Stable Values API resolves this by offering safe wrappers around the `@Stable` annotation, making its benefits available to regular Java developers and third-party library developers. This allows for the creation of lazy Lists and Maps with performance akin to constant values.
👉 [Read more](https://inside.java/2025/07/22/javaone-stablevalues/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
The tech blog post discusses the introduction of a FIPS 140-3 compliant mode in the Go programming language, highlighting its significance for developers. The new feature allows Go to meet the Federal Information Processing Standard (FIPS) 140-3 requirements, which is crucial for applications that require high security standards. By incorporating this built-in, native compliance, Go aims to enhance its appeal to developers working on secure and regulated software projects. The post likely elaborates on how this integration will work and its potential benefits for the Go community.
👉 [Read more](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1-4. With Helm 4 set to release later in the year, attendees are encouraged to engage with Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion. The post provides further details about Helm-related activities scheduled for the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

