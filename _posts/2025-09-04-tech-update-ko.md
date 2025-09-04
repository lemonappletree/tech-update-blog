# 🛠️ 2025-09-04 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Service Account Token Integration for Image Pulls Graduates to Beta
이 블로그 글은 Kubernetes v1.34에서 서비스 계정 토큰 통합이 베타 단계로 승격된 내용을 다루고 있습니다. Kubernetes 커뮤니티는 장기적인 크리덴셜 사용을 줄이고 보안 모범 사례를 발전시키고 있으며, v1.34에서 서비스 계정 토큰을 활용한 이미지 풀링 기능을 개선했습니다. 이번 업데이트로 인해 크리덴셜 제공자는 작업 부하에 맞춘 서비스 계정 토큰을 사용하여 레지스트리 크리덴셜을 얻을 수 있으며, 이는 전통적인 이미지 풀 시크릿보다 안전하고 일시적인 대안을 제공합니다.

베타 단계에서는 'cacheType' 필드가 필수로 추가되어 적절한 캐싱 동작을 보장합니다. 또한, 각 이미지의 풀링 시 해당 작업 부하에 적합한 서비스 계정과의 일치를 검증함으로써 보안이 강화됩니다. Kubernetes 관리자는 이전에 풀링된 이미지에 대한 접근을 서비스 계정을 삭제 및 재생성하여 취소할 수 있습니다.

이 기능에 대한 피드백을 커뮤니티에 요청하고 있으며, 특히 크리덴셜 제공자 구현자들이 새로운 베타 API와 캐싱 메커니즘과의 통합에 대해 의견을 주기를 기대하고 있습니다. Kubernetes Slack의 #sig-auth 채널을 통해 참여할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/03/kubernetes-v1-34-sa-tokens-image-pulls-beta/)

## 🔹 Spring Boot - The Road to GA - Introduction
이 기술 블로그 글은 스프링 포트폴리오의 다음 주요 버전 출시를 준비하는 과정을 소개합니다. 20년이 넘는 역사에서 스프링 부트의 네 번째, 스프링 프레임워크의 일곱 번째 주요 버전이 올해 11월에 출시될 예정입니다. 이번 업데이트에서는 JDK 17을 계속 기반으로 삼고, Jakarta EE 11, Kotlin 2, Jackson 3, JUnit 6 등 다양한 업그레이드를 포함할 예정입니다.

출시 전까지 매주 새로운 기능에 대한 블로그 포스트가 올라올 예정이며, 이에 대한 일정과 주제가 제공됩니다. 이 블로그 시리즈는 커뮤니티의 피드백을 바탕으로 진행되며, 많은 새로운 기능을 소개할 계획입니다. Maven Central에서 미리보기 버전을 사용할 수 있으며, 피드백을 제공할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/02/road_to_ga_introduction)

## 🔹 Docker - You are Doing MCP Wrong: 3 Big Misconceptions
제목: MCP를 잘못 사용하고 있습니다: 3가지 큰 오해

요약: 많은 개발자들이 Model Context Protocol(MCP)을 기존의 API 개념에 맞춰 오해하고 있습니다. 그러나 MCP는 API가 아니며, 도구가 에이전트가 아닙니다. 또한 MCP는 단순한 도구 이상의 것입니다. 이러한 오해는 에이전트 설계, 관찰 가능성, 그리고 비결정적 추론이 결정적 실행과 만나야 하는 "마지막 단계"에서 문제를 일으킵니다. 이 글에서는 이러한 오해가 실무에 어떻게 영향을 미치는지를 설명합니다.
👉 [자세히 보기](https://www.docker.com/blog/mcp-misconceptions-tools-agents-not-api/)

## 🔹 Java - The Inside Java Newsletter: Java 25, AI World, JavaOne 2026!
2025년 8월의 Inside Java 뉴스레터는 9월에 출시될 Java 25, 10월에 열릴 Oracle AI World에서의 Java 세션, 그리고 2026년 3월에 있을 JavaOne 발표에 중점을 두고 있습니다. 또한, Java 사용자 그룹의 최신 업데이트, 커뮤니티 이벤트, 엔지니어링 및 커뮤니티 팟캐스트, 그리고 Java 플랫폼 그룹 개발자의 기술 콘텐츠를 지속적으로 다루고 있습니다. 이 뉴스레터는 Java 개발자 관계 팀이 제작하며, 개발자, 학습자, 교육자, 고객을 위한 다양한 멀티미디어 콘텐츠를 제공하는 learn.java, dev.java, inside.java를 방문해보세요. 뉴스레터 아카이브를 확인하고, 구독하며, 친구에게 공유해보세요!
👉 [자세히 보기](https://inside.java/2025/09/02/inside-java-newsletter/)

## 🔹 Golang - Testing Time (and other asynchronicities)
이 블로그 글은 비동기 코드 테스트와 `testing/synctest` 패키지에 대한 논의를 다루고 있습니다. 2025년 GopherCon Europe에서 같은 제목으로 발표된 내용을 바탕으로 하고 있습니다. 비동기적인 코드를 테스트하는 방법과 관련 패키지의 사용법을 탐구합니다.
👉 [자세히 보기](https://go.dev/blog/testing-time)

## 🔹 Helm - Debian/Ubuntu Helm Apt Repository Move
제목: Debian/Ubuntu Helm Apt 저장소 이동

요약: Apt를 사용하여 Helm을 설치하는 경우, Debian/Ubuntu Helm Apt 저장소가 이전된다는 점에 유의해야 합니다. 이전에는 Balto에서 호스팅되었으나, 이제는 Buildkite에서 호스팅됩니다. 새로운 설치 지침을 참고하여 APT 키와 저장소 참조를 업데이트하세요.
👉 [자세히 보기](https://helm.sh/blog/debian-helm-repository-move/)

