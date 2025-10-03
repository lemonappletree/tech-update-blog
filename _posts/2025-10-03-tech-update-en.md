# 🛠️ 2025-10-03 Tech Update Summary

## 🔹 Kubernetes - Announcing Changed Block Tracking API support (alpha)
The blog post announces the alpha release of the Changed Block Tracking API for Kubernetes. This feature enhances the Kubernetes storage ecosystem by allowing CSI storage drivers to efficiently track changes at the block level in PersistentVolume snapshots, improving backup operations. It identifies allocated and changed blocks between snapshots, which is particularly beneficial for handling large datasets, as it reduces the time, resources, and storage costs associated with full backups. Currently, this support is limited to block volumes, not file volumes. The implementation involves several components like the CSI SnapshotMetadata Service API and external snapshot metadata sidecar. Storage providers and backup solutions need to meet specific requirements to leverage this feature, including implementing necessary APIs and integrating sidecar components. The post encourages users to try out the feature and provides links for more information and getting involved in the project's development.
👉 [Read more](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/)

## 🔹 Spring Boot - A Bootiful Podcast: Dr. Kris De Volder on developer tooling for Spring developers and AI
The blog post introduces a podcast episode featuring Dr. Kris De Volder, a renowned figure in Spring developer tooling. The discussion covers various topics, including developer tools for Spring and the role of artificial intelligence in development.
👉 [Read more](https://spring.io/blog/2025/10/02/a-bootiful-podcast-dr-kris-de-volder)

## 🔹 Docker - From Shell Scripts to Science Agents: How AI Agents Are Transforming Research Workflows
The blog post titled "From Shell Scripts to Science Agents: How AI Agents Are Transforming Research Workflows" discusses how AI agents are revolutionizing the way researchers conduct their work. It paints a picture of a typical late-night research scenario where a scientist is multitasking between various tools and data formats like Jupyter notebooks, Excel sheets, and shell scripts to manage complex tasks such as running protein folding models and parsing experimental data. The post highlights the potential of AI agents to streamline these workflows by automating repetitive tasks, integrating disparate tools, and enabling more efficient data analysis and literature searches, ultimately making research processes more efficient and less error-prone.
👉 [Read more](https://www.docker.com/blog/ai-science-agents-research-workflows/)

## 🔹 Java - Oracle Java Extension for Visual Studio Code Version 24.1.2 Is Now Available!
The blog post announces the release of version 24.1.2 of the Oracle Java Extension for Visual Studio Code. This update includes enhancements and new features for Java developers using VS Code, aimed at improving the development experience and productivity. The post likely provides details about specific improvements and how developers can benefit from them. For more information, readers are encouraged to visit the provided link.
👉 [Read more](https://inside.java/2025/10/01/java-vscode-extension-update/)

## 🔹 Golang - Flight Recorder in Go 1.25
The blog post discusses the introduction of a new diagnostic tool in Go 1.25 called "flight recording." This tool is designed to improve the ability to diagnose and troubleshoot issues in Go applications by capturing detailed execution traces. Flight recording provides developers with insights into application behavior, helping them identify and resolve performance bottlenecks and other issues more efficiently. The post likely details how this tool can be used, its benefits, and how it integrates with existing Go diagnostic tools.
👉 [Read more](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
The blog post discusses the release of the first Alpha version of Helm v4, marking a significant milestone in its development. It outlines the current status of Helm v4, detailing the progress made and the steps remaining before the final release. The post also emphasizes how the community can participate in the development process, encouraging contributions and feedback from users to help refine and improve the final version.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

