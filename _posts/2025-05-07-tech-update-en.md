# 🛠️ 2025-05-07 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: Fine-grained SupplementalGroups Control Graduates to Beta
The blog post discusses the advancement of the `supplementalGroupsPolicy` feature in Kubernetes, which has moved from alpha in version 1.31 to beta in version 1.33. This feature allows for more precise control over supplemental groups in containers, enhancing security, especially for volume access, and improving UID/GID transparency. The post highlights a significant change in behavior with this beta release, urging users to review upgrade considerations and potential impacts on existing setups. The feature addresses issues with implicit group memberships defined in `/etc/group` within container images, which can pose security risks due to unrecorded group IDs. Kubernetes now offers two policies: `Merge` (default, backward-compatible) and `Strict` (excludes implicit GIDs from `/etc/group`). The `Strict` policy requires updated CRI runtimes like containerd v2.0 or later and CRI-O v1.31 or later. The blog advises on handling upgrades to avoid pod rejections and encourages community involvement through SIG Node. For more information, it provides links to relevant Kubernetes documentation and enhancement proposals.
👉 [Read more](https://kubernetes.io/blog/2025/05/06/kubernetes-v1-33-fine-grained-supplementalgroups-control-beta/)

## 🔹 Spring Boot - This Week in Spring - May 6th, 2025
The blog post "This Week in Spring - May 6th, 2025" outlines the author's travel schedule, including events in London, Miami, Tampa, Stockholm, and Barcelona, highlighting their participation in various conferences and talks on Spring. The post emphasizes the upcoming release of Spring AI on May 20th and Spring Boot 3.5 shortly after, marking significant developments in the Spring ecosystem. The author is excited about a talk at Spring I/O with Spring founders Rod Johnson and Juergen Hoeller and a presentation with GraalVM founder Thomas Wuerthinger. The post also includes links to recent updates and resources, such as the release of Spring Cloud 2025.0.0-RC1, Spring AI 1.0.0-M8, and a podcast with Spring instructor Mary Ellen Bowman. Additionally, it features discussions on Spring AI's Model Context Protocol, testing in AI, and a mention of JDK 25's instance main methods moving to final. Links to various tutorials and presentations are provided for further exploration.
👉 [Read more](https://spring.io/blog/2025/05/06/this-week-in-spring-may-6th-2025)

## 🔹 Docker - Securing Model Context Protocol: Safer Agentic AI with Containers
The blog post discusses the growing adoption of Model Context Protocol (MCP) tools and the increasing security concerns that accompany this trend. As MCP tools enhance agent autonomy, they introduce risks related to potential misalignment between the agent's behavior and user expectations, as well as the threat of uncontrolled execution. The article highlights the need to address these security issues to ensure safer use of agentic AI, emphasizing the importance of implementing security measures as MCP tools become more widespread.
👉 [Read more](https://www.docker.com/blog/whats-next-for-mcp-security/)

## 🔹 Java - JEP targeted to JDK 25: 512: Compact Source Files and Instance Main Methods
The blog post discusses JEP 512, which is aimed at JDK 25 and focuses on two main features: Compact Source Files and Instance Main Methods. The proposal suggests improvements for more efficient Java source file management and the introduction of instance main methods that could allow developers to better organize their code. The objective is to enhance the overall developer experience by making Java applications more streamlined and manageable.
👉 [Read more](https://inside.java/2025/05/06/jep512-target-jdk25/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
The blog post discusses improvements in benchmarking for the Go programming language, specifically in version 1.24. It highlights the introduction of `testing.B.Loop`, a new feature designed to make benchmark looping more predictable. This enhancement aims to provide more consistent and reliable benchmarking results, addressing issues with the previous approach. By refining the benchmarking process, developers can better assess performance and optimize their code effectively.
👉 [Read more](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The Helm team is attending KubeCon + CloudNativeCon EU 2025 in London from April 1-4. They will be discussing the upcoming release of Helm 4, which is expected later this year. Attendees are encouraged to participate in talk sessions with Helm maintainers and visit the Helm booth in the Project Pavilion for more information. The blog post provides further details on all Helm-related activities throughout the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

