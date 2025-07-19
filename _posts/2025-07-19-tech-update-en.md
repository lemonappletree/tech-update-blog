# 🛠️ 2025-07-19 Tech Update Summary

## 🔹 Kubernetes - Post-Quantum Cryptography in Kubernetes
The blog post titled "Post-Quantum Cryptography in Kubernetes" discusses the impending shift in cryptography due to quantum computing, which threatens to break current cryptographic standards. To counter this, Post-Quantum Cryptography (PQC) is being developed to secure against both classical and quantum attacks. The article explores the implications of PQC on TLS and Kubernetes, highlighting the need to transition to PQC algorithms as quantum threats loom.

Key points include:

1. **Post-Quantum Cryptography (PQC):** PQC algorithms aim to secure against quantum attacks, with a focus on replacing vulnerable public-key cryptosystems like RSA and ECC. NIST has already standardized some PQC algorithms, such as the Module-Lattice Key Encapsulation Mechanism (ML-KEM).

2. **TLS and PQC:** In TLS, PQC needs to address key exchange and digital signature operations, with an immediate priority on migrating key exchange mechanisms to PQC to prevent future decryption of recorded traffic by quantum computers.

3. **Current PQC Adoption:** The article notes the rapid improvement in PQC support, with Go, major browsers, and OpenSSL introducing support for hybrid schemes like X25519MLKEM768, combining classical and PQC algorithms for secure connections.

4. **Kubernetes and PQC:** Kubernetes v1.33 supports hybrid post-quantum key exchange by default due to its use of Go 1.24, marking a significant step in making Kubernetes quantum-safe without major announcements.

5. **Challenges and Limitations:** Issues such as mismatches in Go versions leading to downgrades, larger packet sizes with PQC, and the slow adoption of PQC digital signatures are discussed. The article emphasizes the importance of awareness and preparation for these challenges to ensure long-term security.

Overall, the post underscores the importance of transitioning to PQC to prepare for quantum threats, highlighting advancements and challenges in the Kubernetes ecosystem.
👉 [Read more](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)

## 🔹 Spring Boot - Spring Data 2025.0.2 and 2024.1.8 released
The tech blog post announces the release of Spring Data versions 2025.0.2 and 2024.1.8, which include dependency upgrades, fixes for regressions, and selected improvements. These updates will be integrated into upcoming Spring Boot releases within the following week. Detailed information about each sub-project's updates, such as Spring Data Commons, JPA, MongoDB, and others, is provided, including links to Javadocs, documentation, and changelogs for each version. The post highlights the efforts of the team and contributors in bringing these updates to the community.
👉 [Read more](https://spring.io/blog/2025/07/18/spring-data-2025-0-2-and-2024-1-8-released)

## 🔹 Docker - GoFiber v3 + Testcontainers: Production-like Local Dev with Air
The blog post discusses the challenges of local development when applications depend on external services, such as databases or message queues. These dependencies can lead to unstable scripts and inconsistent development environments. The post highlights how Fiber v3 and Testcontainers address these issues by integrating real service dependencies into the application's lifecycle. This integration makes the development process more manageable, reproducible, and user-friendly for developers. The upcoming release of Fiber v3 promises to introduce significant improvements in this area, enhancing the local development experience.
👉 [Read more](https://www.docker.com/blog/go-local-dev-fiber-v3-testcontainers/)

## 🔹 Java - JEP targeted to JDK 25: 515: Ahead-of-Time Method Profiling
The blog post discusses JEP 515, which is aimed at being included in JDK 25. This JEP introduces a feature called Ahead-of-Time (AOT) Method Profiling. The primary goal of this feature is to enhance the performance of Java applications by profiling methods ahead of time, allowing for better optimization during runtime. This approach is expected to improve the efficiency and speed of Java applications by providing more precise data for the Just-In-Time (JIT) compiler to use in its optimizations. The post highlights the potential benefits and technical details of integrating AOT Method Profiling into the upcoming JDK 25 release.
👉 [Read more](https://inside.java/2025/07/18/jep515-target-jdk25/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
The blog post discusses the introduction of a built-in, native Federal Information Processing Standard (FIPS) 140-3 compliant mode in the Go programming language. This integration allows developers to use cryptographic modules that meet the FIPS 140-3 security requirements directly within Go, enhancing the language's security capabilities. The update makes it easier for developers to build applications that require compliance with these stringent security standards. The post likely explains the benefits of this feature and how it can be implemented in Go projects.
👉 [Read more](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post discusses the Helm team's participation in the KubeCon + CloudNativeCon EU 2025 event being held in London, UK, from April 1 to 4. The team is excited to engage with attendees about the upcoming Helm 4, which is set to be released later in the year. They invite participants to join discussions with Helm maintainers during talk sessions and to visit their booth in the Project Pavilion for more information about all the Helm-related activities scheduled throughout the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

