# 🛠️ 2025-05-09 Tech Update Summary

## 🔹 Kubernetes - Kubernetes 1.33: Volume Populators Graduate to GA
The blog post announces that Kubernetes volume populators have graduated to general availability (GA) in Kubernetes version 1.33. The `AnyVolumeDataSource` feature gate is now always enabled, allowing users to specify any suitable custom resource as the data source for a PersistentVolumeClaim (PVC). The post details four main enhancements since the beta phase: the populator pod is now optional, new mutator functions have been added to modify Kubernetes resources, flexible metric handling for providers has been introduced, and improvements have been made to clean up temporary resources to prevent potential resource leaks. The post also provides instructions on how to use the feature and discusses future directions and potential feature requests for volume populators, such as multi-sync capabilities and prioritization of data sources. Kubernetes SIG Storage is inviting feedback on specific use cases for this feature.
👉 [Read more](https://kubernetes.io/blog/2025/05/08/kubernetes-v1-33-volume-populators-ga/)

## 🔹 Spring Boot - A Bootiful Podcast: V Körbes on security from the platform on up
In this blog post titled "A Bootiful Podcast: V Körbes on security from the platform on up," the host engages in a conversation with V Körbes from Broadcom. The discussion focuses on security considerations both at the platform level and within applications. This episode is part of a series aimed at Spring enthusiasts.
👉 [Read more](https://spring.io/blog/2025/05/08/a-bootiful-podcast-v-korbes)

## 🔹 Docker - Securing Model Context Protocol: Safer Agentic AI with Containers
The blog post discusses the increasing adoption of Model Context Protocol (MCP) tools, which are primarily used by early adopters but are starting to gain wider use. As these tools become more popular, security concerns are also rising. MCP tools enhance agent autonomy, which can lead to risks such as misalignment between how agents behave and what users expect, as well as the potential for uncontrolled execution. The post emphasizes the need to address these security issues to ensure safer use of agentic AI. The use of containers is suggested as a way to improve the security of MCP systems.
👉 [Read more](https://www.docker.com/blog/whats-next-for-mcp-security/)

## 🔹 Java - Structured Concurrency Revamp in Java 25 - Inside Java Newscast #91
The blog post discusses the updates to the structured concurrency API in Java 25 as proposed in JDK Enhancement Proposal 505. This revamp introduces new features such as configuration options and joiners, which aim to simplify and improve the management of concurrent tasks in Java applications. These enhancements are expected to make Java's concurrency model more robust and easier to use, facilitating better performance and reliability in concurrent programming.
👉 [Read more](https://inside.java/2025/05/08/newscast-91/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
The blog post discusses improvements in benchmarking for the Go programming language, introduced in version 1.24. It highlights the new `testing.B.Loop` feature, which aims to provide more predictable and reliable benchmark results. This enhancement allows developers to write benchmarks that automatically adjust their iterations to achieve a stable and consistent measurement of performance, reducing variability and improving the accuracy of benchmarking in Go applications.
👉 [Read more](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The Helm team is attending KubeCon + CloudNativeCon EU 2025 in London from April 1 to 4. They are working on Helm 4, which is expected to be released later this year. Attendees are encouraged to engage with the Helm maintainers during talk sessions and at the Helm booth in the Project Pavilion to learn more about Helm-related activities throughout the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

