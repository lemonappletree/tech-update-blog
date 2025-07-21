# 🛠️ 2025-07-21 Tech Update Summary

## 🔹 Kubernetes - Post-Quantum Cryptography in Kubernetes
This blog post discusses the significance of Post-Quantum Cryptography (PQC) in the context of Kubernetes, emphasizing the urgency to transition from classical cryptographic algorithms to PQC due to the potential threat posed by quantum computing. The article explains the role of PQC in securing TLS communications, focusing on key exchange and digital signatures, and highlights the current state of PQC adoption in the Kubernetes ecosystem. With the release of Kubernetes v1.33 in April 2025, which uses Go 1.24, the system now supports hybrid post-quantum key exchange by default, specifically the X25519MLKEM768 scheme. However, there are challenges such as Go version mismatches, which can lead to downgrades in cryptographic security, and issues related to the size of PQC public keys, which can affect packet transmission. While PQC key exchange mechanisms are progressing well, the adoption of PQC digital signatures is still developing, with larger keys and slower performance being notable obstacles. The post concludes by underscoring the importance of awareness and understanding of these emerging technologies to ensure the security and longevity of Kubernetes.
👉 [Read more](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)

## 🔹 Spring Boot - Spring Data 2025.0.2 and 2024.1.8 released
The blog post announces the release of Spring Data versions 2025.0.2 and 2024.1.8. These service releases include dependency upgrades, fixes for regressions, and selected improvements. The upcoming Spring Boot releases are expected to incorporate these updates by the following week. The post provides detailed lists of updated components, including Spring Data Commons, JPA, MongoDB, KeyValue, Apache Cassandra, Neo4j, LDAP, REST, Redis, Elasticsearch, Couchbase, and Relational, with links to their respective Javadocs, documentation, and changelogs.
👉 [Read more](https://spring.io/blog/2025/07/18/spring-data-2025-0-2-and-2024-1-8-released)

## 🔹 Docker - GoFiber v3 + Testcontainers: Production-like Local Dev with Air
The blog post discusses the challenges of local development when applications depend on external services such as databases or message queues. These dependencies can result in fragile scripts and inconsistent environments. To address this, Fiber v3 and Testcontainers integrate real service dependencies into the application's lifecycle, making them fully managed, reproducible, and developer-friendly. The upcoming release of Fiber v3 introduces new capabilities to enhance local development, ensuring that developers have a consistent and reliable environment that mimics production conditions.
👉 [Read more](https://www.docker.com/blog/go-local-dev-fiber-v3-testcontainers/)

## 🔹 Java - Java Security Evolution - Out with the Old, In with the New
The blog post discusses the ongoing evolution of security within the Java Platform, emphasizing the need to adapt to emerging threats and weakened cryptographic protocols over time. It highlights key changes in Java security, including the permanent disabling of the Security Manager in JDK 24 and the introduction of support for quantum-resistant algorithms to bolster application security. The post also mentions plans for future enhancements, underscoring Java's commitment to maintaining robust security standards.
👉 [Read more](https://inside.java/2025/07/20/javaone-security/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
The blog post discusses the introduction of a built-in, native FIPS 140-3 compliant mode in the Go programming language. This enhancement means that Go now supports cryptographic operations that meet the Federal Information Processing Standard (FIPS) 140-3, which is important for ensuring secure and standardized cryptographic practices. The new feature aims to provide developers with a reliable and compliant way to implement cryptography in their Go applications, enhancing security and meeting regulatory requirements.
👉 [Read more](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1-4. During the event, they will discuss the upcoming Helm 4, which is set to be released later in the year. Attendees can engage with Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion to learn more about Helm-related activities throughout the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

