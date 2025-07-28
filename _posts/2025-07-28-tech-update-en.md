# 🛠️ 2025-07-28 Tech Update Summary

## 🔹 Kubernetes - Post-Quantum Cryptography in Kubernetes
The blog post discusses the importance of Post-Quantum Cryptography (PQC) in the context of Kubernetes, driven by the potential threat posed by quantum computers to current cryptographic standards. PQC algorithms are designed to be secure against quantum and classical computer attacks. The article highlights the necessity of transitioning to PQC algorithms, particularly for TLS key exchanges, as quantum computers could eventually decrypt recorded encrypted data. The post elaborates on the current state of PQC in Kubernetes, noting that Kubernetes v1.33, released in April 2025, supports hybrid post-quantum key exchanges by default due to its use of Go 1.24, which includes support for the hybrid X25519MLKEM768 scheme. The blog also addresses challenges such as Go version mismatches and packet size issues. While PQC key exchange mechanisms are advancing, PQC digital signatures are less integrated into standard toolchains due to larger key sizes and performance issues. The post underscores the importance of staying informed about these developments to ensure Kubernetes' long-term security in a post-quantum world.
👉 [Read more](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)

## 🔹 Spring Boot - Spring Modulith 2.0 M1 released
The blog post announces the release of Spring Modulith 2.0 M1, which is built on Spring Boot 4 M1 and Spring Framework 7.0 M7. A key feature of this release is the revamped Event Publication Registry, addressing limitations of the previous version. The new registry introduces distinct states for event publications such as “published,” “processing,” “failed,” and “resubmitted,” improving state detection and supporting multi-instance deployments without distributed locking. A staleness monitor is added to handle events stuck in a certain state. The JDBC implementation is updated for the new model, with recommendations for JPA projects to try the JDBC-based registry. Users can still use the legacy registry schema with a specific configuration. The full changelog is available, and feedback is encouraged.
👉 [Read more](https://spring.io/blog/2025/07/26/spring-modulith-2-0-M1-released)

## 🔹 Docker - Docker MCP Catalog: Finding the Right AI Tools for Your Project
The blog post discusses the evolution of large language models (LLMs) from merely generating text to becoming dynamic agents that can execute actions. With this advancement, there is an increasing need for a standardized method to allow LLMs to interact securely with external tools. The Model Context Protocol (MCP) is introduced as a solution, providing a framework to convert existing APIs into tools that are accessible to AI. This initiative aims to enhance the integration of AI with various developer tools, ensuring a secure and efficient interaction.
👉 [Read more](https://www.docker.com/blog/finding-the-right-ai-developer-tools-mcp-catalog/)

## 🔹 Java - A New Model for Java Object Initialization
The blog post discusses advancements in Java object initialization, focusing on the co-evolution of the Java language, JVM, and coding practices. These improvements aim to provide stronger guarantees regarding the initialization of fields, arrays, and objects. Such guarantees help reduce bugs and enable new runtime optimizations. The post highlights the Valhalla project at OpenJDK, which leverages these optimizations for significant performance gains. It also covers the Flexible Constructor Bodies preview feature in Java 24 and outlines planned future language enhancements.
👉 [Read more](https://inside.java/2025/07/27/javaone-object-initialization/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
The blog post announces that Go, the popular programming language, now includes a built-in, native mode that complies with the FIPS 140-3 standard. This update ensures that Go's cryptographic module meets the stringent security requirements set by the Federal Information Processing Standards (FIPS) for cryptographic software, enhancing its security and reliability for developers who need to adhere to these standards.
👉 [Read more](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1st to 4th. The team is working on Helm 4, which is expected to be released later in the year. Attendees are encouraged to participate in discussions with Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion. The post provides more details on Helm-related activities planned for the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

