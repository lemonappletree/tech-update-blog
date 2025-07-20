# 🛠️ 2025-07-20 Tech Update Summary

## 🔹 Kubernetes - Post-Quantum Cryptography in Kubernetes
The blog post discusses the integration of Post-Quantum Cryptography (PQC) within the Kubernetes ecosystem, highlighting its importance due to the potential threat quantum computers pose to current cryptographic standards. It explains the necessity to transition to PQC algorithms, particularly for TLS encryption used in Kubernetes, by incorporating hybrid key exchange mechanisms. With the release of Kubernetes v1.33 in April 2025, the system now defaults to using a hybrid post-quantum key exchange (X25519MLKEM768) by leveraging Go 1.24's capabilities. However, this transition faces challenges, such as Go version mismatches and packet size limitations, which can affect secure communications. While PQC key exchange mechanisms are advancing, the adoption of PQC digital signatures is lagging due to larger key sizes, slower performance, and limited toolchain support. The article emphasizes the need for awareness of these developments to secure Kubernetes in a post-quantum world.
👉 [Read more](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)

## 🔹 Spring Boot - Spring Data 2025.1.0-M4 released
The blog post announces the release of the fourth milestone for the upcoming Spring Data generation, version 2025.1.0-M4, highlighting new features and improvements. Key updates include:

1. **Ahead-of-Time (AOT) Optimizations**: AOT-generated repositories are now enabled by default with Spring Boot's build plugin. Users can disable AOT repository generation for JPA or MongoDB if needed.

2. **MongoDB Enhancements**: The update includes AOT repository support for additional query methods, such as geospatial types, vector search, collations, and value expressions. Default representation for BigDecimal and BigInteger has shifted to Decimal128.

3. **Composite Identifiers in JDBC**: Spring Data JDBC now supports composite identifiers, allowing complex types for IDs with simple properties.

4. **Spring Data Redis**: The update includes JSpecify annotations and Jackson 3-based serializers. Jackson 2 support is now deprecated.

The post also mentions ongoing work on finalizing Jackson 3 support and provides links to detailed release notes and documentation for various Spring Data modules, including JPA, MongoDB, Redis, and more. The community's contribution through issue reports and pull requests is acknowledged.
👉 [Read more](https://spring.io/blog/2025/07/18/spring-data-2025-1-0-M4-released)

## 🔹 Docker - GoFiber v3 + Testcontainers: Production-like Local Dev with Air
The blog post discusses the challenges of local development when applications depend on external services like databases or message queues, which often result in unreliable scripts and inconsistent environments. It highlights how GoFiber v3 and Testcontainers address these issues by integrating real service dependencies into the application's lifecycle, making them fully managed, reproducible, and developer-friendly. The upcoming release of Fiber v3 introduces new features to further enhance this integration, offering a more seamless and efficient local development experience.
👉 [Read more](https://www.docker.com/blog/go-local-dev-fiber-v3-testcontainers/)

## 🔹 Java - JEP targeted to JDK 25: 515: Ahead-of-Time Method Profiling
The tech blog post discusses JEP 515, which is aimed at being included in JDK 25. This JEP focuses on "Ahead-of-Time Method Profiling," a technique intended to enhance the performance of Java applications. By collecting method profiling data before execution, this approach aims to optimize the execution process, potentially leading to more efficient Java applications. The post likely provides details about the implementation and potential benefits of this feature for Java developers.
👉 [Read more](https://inside.java/2025/07/18/jep515-target-jdk25/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
The blog post discusses the introduction of a built-in, native FIPS 140-3 compliant mode in the Go programming language. This development means that Go now supports cryptographic operations that meet the Federal Information Processing Standard (FIPS) 140-3, which is important for ensuring secure and reliable cryptographic implementations. The post likely details how this compliance is implemented in Go, its benefits for developers, and its impact on security and cryptographic practices within Go applications.
👉 [Read more](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1-4. They are working on Helm 4, which is set to be released later in the year. Attendees are encouraged to engage with the Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion. The post provides more details on Helm-related activities happening throughout the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

