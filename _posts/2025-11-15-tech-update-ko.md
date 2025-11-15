# 🛠️ 2025-11-15 기술 업데이트 요약

## 🔹 Kubernetes - Ingress NGINX Retirement: What You Need to Know
이 기술 블로그 글은 Kubernetes SIG Network와 보안 대응 위원회가 Ingress NGINX의 퇴출을 발표한 내용입니다. Ingress NGINX는 2026년 3월까지 유지 보수되며 이후에는 추가 릴리스, 버그 수정 또는 보안 취약점 해결이 이루어지지 않을 예정입니다. 현재 배포된 Ingress NGINX는 계속 작동하고 설치 아티팩트도 여전히 사용할 수 있습니다. 사용자는 Gateway API나 다른 Ingress 컨트롤러로의 마이그레이션을 권장합니다. Ingress NGINX는 Kubernetes 프로젝트의 초기 인그레스 컨트롤러로서 유연성과 기능성으로 인기를 끌었으나, 유지 보수의 어려움과 보안 문제로 인해 퇴출이 결정되었습니다. 사용자들은 가능한 빨리 Gateway API나 대체 인그레스 컨트롤러로 전환해야 합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)

## 🔹 Spring Boot - Spring Data 2025.1.0 goes GA
이 기술 블로그 글에서는 Spring Data 2025.1.0의 정식 출시를 발표하고 있습니다. 주요 기능으로는 Spring Framework 7 및 Jakarta EE 11로의 업그레이드, AOT(사전 컴파일) 리포지토리, JSpecify를 통한 포괄적인 null 안전성, Jackson 3 지원, 그리고 벡터 검색 메서드를 포함합니다. AOT 리포지토리는 시작 시간을 단축하고 메모리 사용량을 줄이며, JSpecify는 코드 품질을 개선합니다. Jackson 3은 기존 Jackson 2와 호환성을 유지하면서도 새로운 기능을 제공합니다. 벡터 검색은 AI 문맥에서 기존 데이터 모델을 사용할 수 있도록 합니다. 자세한 내용은 릴리즈 노트를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/14/spring-data-2025-1-goes-ga)

## 🔹 Docker - Making the Most of Your Docker Hardened Images Trial – Part 1
블로그 글 "Making the Most of Your Docker Hardened Images Trial – Part 1"의 요약:

이 글은 Docker Hardened Images를 활용하여 첫 번째 보안 및 프로덕션 준비 상태의 이미지를 실행하는 방법에 대해 설명합니다. 컨테이너 기반 이미지는 애플리케이션 보안의 기초를 이루며, 기초에 취약점이 있으면 그 위에 구축된 모든 서비스가 동일한 위험을 안게 됩니다. Docker Hardened Images는 이러한 문제를 해결하기 위해 설계되었으며, 불필요한 패키지를 제거하고 사전적으로 패치를 적용하여 보안을 강화한 최소한의 기본 이미지입니다.
👉 [자세히 보기](https://www.docker.com/blog/making-the-most-of-your-docker-hardened-images-trial-part-1/)

## 🔹 Java - Deep Dive into Gatherers - JEP Cafe #24
이 기술 블로그 글은 JDK 24에 추가되고 JDK 25에서 사용할 수 있는 "Gatherers"에 대해 심도 있게 다루고 있습니다. 이 글에서는 매핑과 필터링의 기본, 내부 변경 가능한 상태를 생성 및 관리하여 스트림을 제한하고 정렬하는 방법을 다양한 예제와 함께 설명합니다. 또한 스트림을 적절히 중단하는 방법, API 사용 시 리소스 누수와 경쟁 조건을 피하는 방법, 그리고 최적화를 활용하는 방법을 다룹니다. 스트림 API의 주요 기능 중 하나는 병렬 처리가 가능하다는 점인데, 병렬 Gatherers와 병렬 스트림에서 비병렬 Gatherers의 사용 방법도 설명합니다. 이 비디오를 통해 효율적이고 올바른 Gatherers를 작성하는 데 필요한 모든 것을 배우고, 언제 Gatherers를 사용해야 하는지, 그리고 언제 피해야 하는지 알게 될 것입니다.
👉 [자세히 보기](https://inside.java/2025/11/14/jepcafe24/)

## 🔹 Golang - Go’s Sweet 16
블로그 글 "Go’s Sweet 16"은 프로그래밍 언어 Go의 16번째 생일을 축하하는 내용입니다. 글에서는 Go 언어의 발전과 성과를 되돌아보며, 그동안 Go 커뮤니티가 이룬 성과를 강조하고 있습니다. 또한 Go의 미래에 대한 기대와 앞으로의 계획에 대해서도 간단히 언급하고 있습니다.
👉 [자세히 보기](https://go.dev/blog/16years)

