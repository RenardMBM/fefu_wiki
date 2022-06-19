<script lang="ts">
import { defineComponent, PropType} from 'vue';
import TeacherItem from "@/components/TeacherItem.vue";
import ContentBlock from "@/components/UI/ContentBlock.vue";
import PageTitle from "@/components/UI/PageTitle.vue";
import MySubtitle from "@/components/UI/MySubtitle.vue";
import Teacher from "@/models/TeacherItemModel";

export default defineComponent({
  name: "TopTeachers",
  components: {
    TeacherItem,
    ContentBlock,
    PageTitle,
    MySubtitle
  },
  props: {
    title: {
      type: String,
      required: true,
    },
    teachers: {
      type: Array as PropType<Array<Teacher>>,
      required: true,
    }
  }
})
</script>

<template>
  <content-block class="top-column">
    <div class="top-title">
      {{title}}
    </div>
    <div class="top-list" v-if="teachers.length > 0">
      <teacher-item class="top-list-item"
          v-for="teacher in teachers"
          :teacher="teacher"
      />
    </div>
    <div class="top-list-item" v-else >
      Список пуст
    </div>
  </content-block>
</template>

<style scoped>
.top-title{
  font-size: 18px;
  text-align: center;
}
.top-column{
  padding-bottom: 0.5em;
  width: fit-content!important;
}
.top-list{
  padding-top: 1em;
  display: inline-block;
  /*padding: 1em;*/
}
.top-list-item{
  margin-bottom: 0.5em;
}
</style>