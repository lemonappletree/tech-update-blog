# 🛠️ 2025-07-24 Tech Update Summary

## 🔹 Kubernetes - Post-Quantum Cryptography in Kubernetes
The blog post discusses the implications of post-quantum cryptography (PQC) for the Kubernetes ecosystem in the context of the potential threat posed by quantum computers to current cryptographic standards. It explains that PQC algorithms are designed to be secure against both classical and quantum attacks, with a focus on their integration into TLS (Transport Layer Security). The post highlights that, due to the adoption of Go 1.24 in Kubernetes v1.33, the system now supports the hybrid post-quantum key exchange mechanism X25519MLKEM768 by default. This adoption is a significant step towards making Kubernetes quantum-safe. The post also addresses challenges such as the larger key sizes associated with PQC and the importance of understanding Go version mismatches, which could lead to downgrades in cryptographic security. Although PQC key exchange mechanisms are seeing broader adoption, PQC digital signatures still face hurdles due to larger key sizes, slower performance, and limited toolchain support. The article concludes that while Kubernetes is making strides towards post-quantum security, continued awareness and adaptation are necessary for long-term security.
👉 [Read more](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)

## 🔹 Spring Boot - Spring Batch 6.0.0-M1 is out!
The blog post announces the release of Spring Batch 6.0.0-M1, highlighting its new features, enhancements, and bug fixes. Key changes include upgraded dependencies like Spring Framework 7.0 and Micrometer 1.16, improvements in batch infrastructure configuration with new annotations for job repositories, a default resourceless batch infrastructure, and simplified configuration. A new command line job operator replaces the older version for better extensibility. The release involves deprecations and removals of older APIs to streamline the core functionality. Users are encouraged to review the release notes and migration guide for detailed changes and to provide feedback via GitHub or social media.
👉 [Read more](https://spring.io/blog/2025/07/23/spring-batch-6)

## 🔹 Docker - Docker MCP Catalog: Finding the Right AI Tools for Your Project
The blog post discusses the evolution of large language models (LLMs) from being static text generators to becoming dynamic agents that can execute actions. With this evolution, there is an increased need for a standardized method to allow these models to securely interact with external tools. The post introduces the Model Context Protocol (MCP), which is designed to convert existing APIs into tools that can be accessed by AI. This protocol helps in finding the right AI tools for various projects by making APIs more accessible to advanced AI models.
👉 [Read more](https://www.docker.com/blog/finding-the-right-ai-developer-tools-mcp-catalog/)

## 🔹 Java - A Sneak Peek at the Stable Values API
The blog post introduces the Stable Values API, which addresses the limitations of the internal `@Stable` annotation in Java. Previously, the `@Stable` annotation, used within internal JDK classes to mark fields with values that change at most once, offered significant performance, energy efficiency, and flexibility benefits. However, its use was restricted to internal applications. The new Stable Values API provides safe wrappers around the `@Stable` annotation, making its advantages accessible to regular Java developers and third-party library developers. This allows developers to create lazy Lists and Maps with performance akin to constant values.
👉 [Read more](https://inside.java/2025/07/22/javaone-stablevalues/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
The blog post discusses the introduction of a native FIPS 140-3 compliant mode in the Go programming language. This update means that Go now includes a built-in cryptographic module that adheres to the FIPS 140-3 standard, which is a U.S. government standard for cryptographic modules used to protect sensitive information. The integration of this compliance mode enhances the security capabilities of Go, making it more suitable for use in environments that require stringent security standards.
👉 [Read more](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London, UK, from April 1 to 4. During the event, they will discuss the upcoming release of Helm 4, which is expected later in the year. Attendees can engage with Helm maintainers during talk sessions and visit the Helm booth at the Project Pavilion for more information. The post encourages attendees to participate in Helm-related activities throughout the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

