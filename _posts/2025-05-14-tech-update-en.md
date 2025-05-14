# 🛠️ 2025-05-14 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: Job's Backoff Limit Per Index Goes GA
The blog post discusses the Kubernetes v1.33 update, where the "Backoff Limit Per Index" feature has reached general availability (GA). This feature is crucial for managing workloads in Kubernetes, particularly in scenarios where pod failures can impact workload completion. Traditionally, the `spec.backoffLimit` field was used to set a total number of tolerated failures. However, this wasn't flexible enough for workloads where each index operates independently, like embarrassingly parallel workloads. The new "Backoff Limit Per Index" allows more granular control by setting a retry limit per index, using the `spec.backoffLimitPerIndex` field. This feature helps prevent a fast-failing index from consuming the entire failure tolerance budget. The blog also explains how to use this feature in combination with the "Pod Failure Policy" to handle errors more effectively, providing an example job spec for illustration. Additionally, it encourages readers to learn more through related resources and get involved with the Kubernetes community.
👉 [Read more](https://kubernetes.io/blog/2025/05/13/kubernetes-v1-33-jobs-backoff-limit-per-index-goes-ga/)

## 🔹 Spring Boot - Spring AI 1.0.0 RC1 Released
The tech blog post announces the release of Spring AI 1.0.0 RC1, which is the final release candidate before the stable version scheduled for release on May 20, 2025. The release includes breaking changes, bug fixes, and new features. The team will focus on improving documentation and resolving reported bugs before the general availability (GA) release. Key updates include naming standardization, observability changes, and model enhancements with integrations such as DeepSeek and Azure OpenAI. New features also involve RAG and document processing improvements, enhanced memory management, and logging observability. The post celebrates the release with an AI-generated music playlist and acknowledges numerous contributors to the project. Important links for upgrade notes and migration guides are provided, along with instructions for automating the upgrade process.
👉 [Read more](https://spring.io/blog/2025/05/13/spring-ai-1-0-0-RC1-released)

## 🔹 Docker - Securing Model Context Protocol: Safer Agentic AI with Containers
The blog post titled "Securing Model Context Protocol: Safer Agentic AI with Containers" discusses the emerging importance of securing Model Context Protocol (MCP) tools as their adoption increases. While currently primarily used by early adopters, these tools are being adopted more broadly, which is raising urgent security concerns. The increased autonomy that MCP tools provide to agents can lead to risks, such as misalignment between agent actions and user expectations as well as uncontrolled execution. The post suggests that these systems introduce new challenges in ensuring secure and safe use as they become more widespread.
👉 [Read more](https://www.docker.com/blog/whats-next-for-mcp-security/)

## 🔹 Java - JEP targeted to JDK 25: 505: Structured Concurrency (5th Preview)
The tech blog post discusses JEP 505, which is targeted for JDK 25 and focuses on structured concurrency. This is the fifth preview of the proposal. Structured concurrency aims to simplify multithreaded programming by introducing a new concurrency model that organizes and manages thread lifecycles more systematically. The proposal seeks to improve the readability and maintainability of concurrent code and to reduce common concurrency-related bugs by treating groups of threads as structured units. This approach can lead to more reliable and easier-to-understand concurrent applications.
👉 [Read more](https://inside.java/2025/05/12/jep505-target-jdk25/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
The tech blog post discusses enhancements in benchmarking for the Go programming language with the introduction of `testing.B.Loop` in Go 1.24. This new feature aims to improve the predictability and consistency of benchmark results. By providing a more structured way to loop benchmarks, `testing.B.Loop` helps developers achieve more reliable performance testing outcomes, making it easier to identify genuine performance changes in their code.
👉 [Read more](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London, UK, from April 1-4. They will be discussing the upcoming release of Helm 4, which is planned for later in the year. Attendees are encouraged to participate in discussions with Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion. The post provides more details on Helm-related activities happening throughout the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

