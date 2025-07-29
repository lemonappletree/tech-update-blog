# 🛠️ 2025-07-29 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.34 Sneak Peek
The blog post provides a preview of the upcoming Kubernetes v1.34 release, expected at the end of August 2025. This release includes several enhancements without any removals or deprecations. Key features include:

1. **Dynamic Resource Allocation (DRA)**: Graduating to stable, DRA offers flexible device management in clusters, supporting structured parameters and central device categorization.
   
2. **ServiceAccount Tokens for Image Pull Authentication**: Likely reaching beta, this feature uses short-lived tokens for secure image registry access, reducing the need for long-lived secrets.
   
3. **Pod Replacement Policy for Deployments**: An alpha feature introducing policies to manage pod replacements during updates, offering faster rollouts or controlled resource usage.
   
4. **Production-ready Tracing**: Tracing for `kubelet` and API Server aims for stable status, enhancing debugging with OpenTelemetry for end-to-end event visualization.
   
5. **Traffic Distribution Preferences**: The `PreferSameZone` and `PreferSameNode` options improve traffic routing within Services, set to reach beta.
   
6. **KYAML Support**: A new YAML subset designed for Kubernetes, ensuring compatibility and addressing YAML's limitations, with expected integration in `kubectl`.
   
7. **Fine-grained Autoscaling Control**: A customizable HPA tolerance feature targeting beta, allowing varied tolerance settings for scale operations, optimizing resource usage.

The post also invites community involvement through SIGs, discussions, and meetings, and encourages following updates on various platforms. The official release notes will further outline v1.34's new features and changes.
👉 [Read more](https://kubernetes.io/blog/2025/07/28/kubernetes-v1-34-sneak-peek/)

## 🔹 Spring Boot - Spring Modulith 2.0 M1 released
The blog post announces the release of Spring Modulith 2.0 M1, which is based on the latest Spring Boot 4 M1 and Spring Framework 7.0 M7. A key feature of this release is the revamped Event Publication Registry, which addresses limitations of the previous version. The registry now includes new states such as "published," "processing," "failed," and "resubmitted," allowing better differentiation and handling of event publications. The JDBC implementation has been updated to support this new model, and other store modules have been adjusted to maintain compatibility with existing applications. A staleness monitor has been introduced to handle publications that get stuck in certain states. The post encourages users to try the new version and provide feedback, offering guidance for those using legacy registry schemas. The full changelog is available on GitHub.
👉 [Read more](https://spring.io/blog/2025/07/26/spring-modulith-2-0-M1-released)

## 🔹 Docker - Beyond the Chatbot: Event-Driven Agents in Action
The blog post titled "Beyond the Chatbot: Event-Driven Agents in Action" discusses a recent 24-hour hackathon held by Docker with the objective of developing an agent to enhance productivity. The author reflects on the desire to avoid spending more time in chat interfaces, proposing the creation of a fully automated agent that operates independently without requiring human interaction. The idea is to move beyond traditional chatbots by implementing event-driven agents that can autonomously perform tasks and improve efficiency.
👉 [Read more](https://www.docker.com/blog/beyond-the-chatbot-event-driven-agents-in-action/)

## 🔹 Java - Episode 39 “Deprecations &amp; Removals” with Stuart Marks
In episode 39 of the podcast, titled "Deprecations & Removals," Stuart Marks discusses the process of removing outdated features from Java. The episode highlights the importance of eliminating obsolete components that can be a maintenance burden, affect performance, or pose security risks. Specific topics include the removal of 32-bit ports, applets, the finalization mechanism, and the security manager. The discussion emphasizes Java's ongoing efforts to streamline and enhance the platform by phasing out features that are no longer necessary or safe to use.
👉 [Read more](https://inside.java/2025/07/28/podcast-039/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
The blog post announces that the Go programming language now includes a built-in, native mode that complies with FIPS 140-3, which is a U.S. government standard for cryptographic modules. This enhancement means that developers using Go can now ensure their applications meet stringent security requirements without needing external libraries or additional configurations. The integration aims to simplify the development process for secure applications while maintaining high standards of data protection.
👉 [Read more](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1 to 4. The team is working on Helm 4, which is expected to be released later in the year. Attendees are encouraged to participate in discussions with Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion. The post provides details on all Helm-related activities happening throughout the conference week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

