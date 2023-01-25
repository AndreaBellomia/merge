<template>
  <div class="flex-row">
    <div
      class="
        flex
        bg-violet-600
        text-slate-100
        justify-start
        px-5
        align-middle
        py-4
        text-2xl
        font-semibold
      "
    >
      <p>Prenotazione</p>
    </div>

    <div class="grid grid-cols-3 bg-neutral-50 gap-3 p-5">
      <div class="p-3 bg-neutral-300 rounded-lg">
        <div class="">
          <p>25 Gennaio 2023</p>
        </div>
      </div>
      <div class="col-span-2 bg-neutral-300 rounded-lg p-3">
        <label
            for="header"
            class="block mb-2 text-gray-900 font-semibold"
            >Titolo</label
            >
        <input type="text" name="" id="header" class="text-sm w-full rounded-lg p-2 focus:ring-blue-500 focus:border-blue-500" placeholder="Inserisci un titilo ..."/>
      </div>
      <div class="col-span-3 bg-neutral-300 rounded-lg p-2">
        <label
          for="message"
          class="block mb-2 font-semibold text-gray-900 "
          >Descrizione</label
        >
        <textarea
          id="message"
          rows="6"
          cols="108"
          class="
            block
            p-2.5
            w-full
            text-sm text-gray-900
            bg-neutral-50
            rounded-lg
            border border-gray-300
            focus:ring-blue-500 focus:border-blue-500
          "
          placeholder="Inserisci una descrizione ..."
        ></textarea>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>